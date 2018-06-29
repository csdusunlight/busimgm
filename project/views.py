from rest_framework import generics, permissions
from project.models import Project
from project.serializers import ProjectSerializer
from project.Filters import ProjectFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django.urls.base import reverse

import django_filters
from django.http.response import Http404, JsonResponse, HttpResponse
from project.models import ProjectInvestData
from django.views.decorators.csrf import csrf_exempt
import xlrd
import logging
from django.db import transaction
from decimal import Decimal

from xlwt.Workbook import Workbook
from xlwt.Style import easyxf
import traceback
import datetime
from tools.StringIO import StringIO
from project.models import DBlock
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response


logger = logging.getLogger('wafuli')


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectFilter
    ordering_fields = ('uname')
    search_fields = ('uname')
    ordering=('time')
    def perform_create(self, serializer):
        serializer.save()
        print(serializer)

        data = serializer.data
        serializer._data = {}
        serializer._data['code'] = 0
        serializer._data['data'] = data


from rest_framework.decorators import action
from rest_framework import viewsets





class ProjectDetail(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    '''三个操作分别是修改，删除，结项申请，都是商务人员发起的'''


    @action(methods=['patch'],detail=True)
    def project_to_be_applyed(self, request,pk=None,*args,**kwargs):
        '''修改的字段仅仅限于几个字段'''
        print(self.get_view_name())
        print(request.data)
        #print(self.)

        print(pk)
        self.partial_update(request,*args,**kwargs)
        return Response("hi1")

    @action(methods=['patch'],detail=True)
    def project_to_be_altered(self, request, pk=None,*args,**kwargs):
        '''删除的字段仅仅限于is_delete'''
        self.partial_update(request, *args, **kwargs)
        return Response("hi2")
        # judgeres = [True if i == "is_delete" else False for i in request.data ]
        # print(judgeres)
        # if all(judgeres)==True:
        #     self.partial_update(request,*args,**kwargs)
        # else:
        #     raise Exception("do not pass no need para!")


        # aimPro=Project.objects.get(id=pk)
        # aimPro.settle=100
        # aimPro.save(update_fields=['settle',])
        return Response("hi2")

    @action(methods=['patch'],detail=True)
    def project_to_be_deleted(self, request, pk=None,*args,**kwargs):
        self.partial_update(request,*args,**kwargs)
        aimPro=Project.objects.get(id=pk)
        aimPro.consume=100
        aimPro.save(update_fields=['consume',])
        return Response("hi3")

def approve_for_project_apply(request,*args,**kwargs):
    '''关于批准立项的操作是由更改project的状态field ,审核人员的单独的权限'''
    id = kwargs['pk']
    admin_user = request.user
    aimPro = Project.objects.get(id=id)
    aimPro.auditstate = '1'
    aimPro.audituser = admin_user
    aimPro.save(update_fields=['auditstate','audituser'])
    return Response("end")







#def finish_project(request):
    '''结项的操作是发出申请后
    结项的操作是更改project的状态，并且计算结算金额'''




def import_projectdata_excel(request):
    admin_user = request.user
    if not (admin_user.is_authenticated() and admin_user.is_staff):
        raise Http404
    ret = {'code': -1}
    file = request.FILES.get('file')
    #     print file.name
    with open('./out.xls', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    data = xlrd.open_workbook('./out.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    if ncols != 8:
        ret['msg'] = "文件格式与模板不符，请下载最新模板填写！"
        return JsonResponse(ret)
    rtable = {}
    mobile_list = []
    dup = {}
    try:
        for i in range(1, nrows):
            temp = []
            for j in range(ncols):
                cell = table.cell(i, j)
                value = cell.value
                if j == 0:
                    id = int(value)
                    project = Project.objects.get(id=id)
                    temp.append(id)
                elif j == 2:
                    value = value.strip()
                    if value == u"首投":
                        temp.append(False)
                    elif value == u"复投":
                        temp.append(True)
                    else:
                        raise Exception(u"必须为首投或复投。")
                elif j == 3:
                    if (cell.ctype != 3):
                        raise Exception("投资日期列格式错误，请修改后重新提交。")
                    else:
                        time = xlrd.xldate.xldate_as_datetime(value, 0)
                        temp.append(time)
                elif j == 4:
                    try:
                        mobile = str(int(value)).strip()
                    except Exception as e:
                        mobile = str(value).strip()
                    if len(mobile) == 11:
                        temp.append(mobile)
                    else:
                        raise Exception("手机号必须是11位，请修改后重新提交。")
                elif j == 5 or j == 7:
                    try:
                        temp.append(Decimal(value))
                    except:
                        raise Exception("投资金额必须为数字")
                elif j == 6:
                    try:
                        temp.append(int(value))
                    except Exception as e:
                        raise Exception("投资标期必须为数字，请修改后重新提交。")
                else:
                    temp.append(value)
            tid = temp[0]
            if not temp[2]:
                if dup.has_key(tid):
                    if temp[4] in dup[tid]:
                        continue
                    else:
                        dup[tid].append(temp[4])
                else:
                    dup[tid] = [temp[4], ]

            if rtable.has_key(tid):
                rtable[tid].append(temp)
            else:
                rtable[tid] = [temp, ]
    except Exception as e:

        logger.info(e)
        #             traceback.print_exc()
        ret['msg'] = e
        return JsonResponse(ret)
    ####开始去重
    investdata_list = []
    duplicate_mobile_list = []
    try:
        with transaction.atomic():
            db_key = DBlock.objects.select_for_update().get(index='investdata')
            for id, values in rtable.items():
                temp = ProjectInvestData.objects.filter(project_id=id).values('invest_mobile')
                db_mobile_list = map(lambda x: x['invest_mobile'], temp)
                for item in values:
                    pid = item[0]
                    time = item[3]
                    mob = item[4]
                    is_futou = item[2]
                    amount = item[5]
                    term = item[6]
                    settle = item[7]
                    source = ''
                    remark = ''
                    if not is_futou and mob in db_mobile_list:
                        duplicate_mobile_list.append(mob)
                    else:
                        obj = ProjectInvestData(project_id=pid, invest_mobile=mob, settle_amount=settle,
                                                invest_amount=amount, invest_term=term, invest_time=time,
                                                state='1', remark=remark, source=source, is_futou=is_futou)
                        investdata_list.append(obj)
            ProjectInvestData.objects.bulk_create(investdata_list)
    except Exception as e:
        logger.info(e)
        #             traceback.print_exc()
        ret['msg'] = e
        return JsonResponse(ret)
    succ_num = len(investdata_list)
    duplic_num2 = len(duplicate_mobile_list)
    duplic_num1 = nrows - 1 - succ_num - duplic_num2
    duplic_mobile_list_str = u'，'.join(duplicate_mobile_list)
    ret.update(code=0, num=succ_num, dup1=duplic_num1, dup2=duplic_num2, anum=nrows - 1, dupstr=duplic_mobile_list_str)
    return JsonResponse(ret)


def import_audit_projectdata_excel(request):
    admin_user = request.user
    if not (admin_user.is_authenticated() and admin_user.is_staff):
        raise Http404
    ret = {'code': -1}
    file = request.FILES.get('file')
    #     print file.name
    with open('./out2.xls', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    data = xlrd.open_workbook('./out2.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    if ncols != 13:
        ret['msg'] = u"文件格式与模板不符，请下载最新模板填写！"
        return JsonResponse(ret)
    rtable = []
    try:
        for i in range(1, nrows):
            row = table.row_values(i)
            temp = {}
            id = int(row[0])
            project_id = int(row[1])
            term = int(row[7])
            mobile = row[5]
            consume = Decimal(row[8])
            remark = row[12]
            date = row[4]
            date = xlrd.xldate.xldate_as_datetime(date, 0)

            try:
                mobile = str(int(mobile)).strip()
            except Exception as e:
                mobile = str(mobile).strip()
            if len(mobile) != 11:
                raise Exception(u"手机号必须是11位，请修改后重新提交。")
            if row[9] == "是":
                result = True
                temp['state'] = '0'
            elif row[9] == "否":
                result = False
                temp['state'] = '1'
            else:
                raise Exception(u"审核结果必须为是或否。")

            if row[10]:
                return_amount = Decimal(row[10])
                if return_amount > consume:
                    raise Exception(u"返现金额不能大于结算金额，请检查表格")
            elif result:
                raise Exception(u"审核结果为是时，返现金额不能为空或零。")
            else:
                return_amount = 0

            if row[11] == "网站":
                source = 'site'
            elif row[11] == "渠道":
                source = 'channel'
            else:
                raise Exception(u"必须为网站或渠道。")
            temp['id'] = id
            temp['project_id'] = project_id
            temp['source'] = source
            temp['return_amount'] = return_amount
            temp['consume'] = consume
            temp['remark'] = remark
            temp['mobile'] = mobile
            temp['date'] = date
            temp['term'] = term
            rtable.append(temp)
    except Exception as  e:
        logger.info(e)
        #             traceback.print_exc()
        ret['msg'] = e
        return JsonResponse(ret)
        ####开始去重
        admin_user = request.user
    suc_num = 0
    try:
        for row in rtable:
            id = row['id']
            return_amount = row['return_amount']
            source = row['source']
            remark = row['remark']
            mobile = row['mobile']
            consume = row['consume']
            project_id = row['project_id']
            state = row['state']
            date = row['date']
            term = row['term']
            event = ProjectInvestData.objects.get(id=id)
            #             if event.state != '1':
            #                 continue
            event.state = state
            event.return_amount = return_amount
            event.audit_time = datetime.datetime.now()
            event.source = source
            event.remark = remark
            event.settle_amount = consume
            event.project_id = project_id
            event.invest_mobile = mobile
            event.invest_time = date
            event.invest_term = term
            event.save(update_fields=['state', 'return_amount', 'audit_time', 'source', 'remark', 'invest_term',
                                      'project_id', 'settle_amount', 'invest_mobile', 'invest_time'])
            suc_num += 1
        ret['code'] = 0
    except Exception as e:
        exstr = traceback.format_exc()
        logger.info(unicode(exstr))
        ret['code'] = 1
        ret['msg'] = unicode(e)
    ret['num'] = suc_num
    return JsonResponse(ret)


def import_audit_projectdata_excel_except(request):
    admin_user = request.user
    if not (admin_user.is_authenticated() and admin_user.is_staff):
        raise Http404
    ret = {'code': -1}
    file = request.FILES.get('file')
    #     print file.name
    with open('./out2.xls', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    data = xlrd.open_workbook('./out2.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    if ncols != 13:
        ret['msg'] = u"文件格式与模板不符，请下载最新模板填写！"
        return JsonResponse(ret)
    rtable = []
    try:
        for i in range(1, nrows):
            row = table.row_values(i)
            temp = {}
            id = int(row[0])
            project_id = int(row[1])
            mobile = row[5]
            consume = Decimal(row[8])
            remark = row[12]
            date = row[4]
            date = xlrd.xldate.xldate_as_datetime(date, 0)

            if row[9] == "是":
                result = True
                temp['state'] = '0'
            elif row[9] == "否":
                result = False
                temp['state'] = '1'
            else:
                raise Exception(u"审核结果必须为是或否。")

            if row[10]:
                return_amount = Decimal(row[10])
            else:
                return_amount = 0

            if row[11] == "网站":
                source = 'site'
            elif row[11] == "渠道":
                source = 'channel'
            else:
                raise Exception(u"必须为网站或渠道。")
            temp['id'] = id
            temp['project_id'] = project_id
            temp['source'] = source
            temp['return_amount'] = return_amount
            temp['consume'] = consume
            temp['remark'] = remark
            temp['mobile'] = mobile
            temp['date'] = date
            rtable.append(temp)
    except Exception as e:
        logger.info(e)
        ret['msg'] = e
        return JsonResponse(ret)
        ####开始去重
        admin_user = request.user
    suc_num = 0
    try:
        for row in rtable:
            id = row['id']
            return_amount = row['return_amount']
            source = row['source']
            remark = row['remark']
            mobile = row['mobile']
            consume = row['consume']
            project_id = row['project_id']
            state = row['state']
            date = row['date']
            event = ProjectInvestData.objects.get(id=id)
            #             if event.state != '1':
            #                 continue
            event.state = state
            event.return_amount = return_amount
            event.audit_time = datetime.datetime.now()
            event.source = source
            event.remark = remark
            event.settle_amount = consume
            event.project_id = project_id
            event.invest_mobile = mobile
            event.invest_time = date
            event.save(update_fields=['state', 'return_amount', 'audit_time', 'source', 'remark',
                                      'project_id', 'settle_amount', 'invest_mobile', 'invest_time'])
            suc_num += 1
        ret['code'] = 0
    except Exception as e:
        exstr = traceback.format_exc()
        logger.info(unicode(exstr))
        ret['code'] = 1
        ret['msg'] = unicode(e)
    ret['num'] = suc_num
    return JsonResponse(ret)



def export_investdata_excel(request):
    user = request.user
    item_list = ProjectInvestData.objects
    is_futou = request.GET.get("is_futou", None)
    if is_futou == "true":
        item_list = item_list.filter(is_futou=True)
    elif is_futou == "false":
        item_list = item_list.filter(is_futou=False)
    state = request.GET.get("state", None)
    if state:
        item_list = item_list.filter(state=state)
    source = request.GET.get("source", None)
    if source:
        item_list = item_list.filter(source=source)
    invest_mobile = request.GET.get("invest_mobile", None)
    if invest_mobile:
        item_list = item_list.filter(invest_mobile=invest_mobile)
    name__contains = request.GET.get("name__contains", None)
    if name__contains:
        item_list = item_list.filter(project__name__contains=name__contains)
    project = request.GET.get("project_id", None)
    if project:
        item_list = item_list.filter(project_id=project)
    investtime_0 = request.GET.get("investtime_0", None)
    investtime_1 = request.GET.get("investtime_1", None)
    audittime_0 = request.GET.get("audittime_0", None)
    audittime_1 = request.GET.get("audittime_1", None)
    if investtime_0 and investtime_1:
        s = datetime.datetime.strptime(investtime_0, '%Y-%m-%d')
        e = datetime.datetime.strptime(investtime_1, '%Y-%m-%d')
        item_list = item_list.filter(invest_time__range=(s, e))
    if audittime_0 and audittime_1:
        s = datetime.datetime.strptime(audittime_0, '%Y-%m-%d')
        e = datetime.datetime.strptime(audittime_1, '%Y-%m-%d')
        item_list = item_list.filter(audit_time__range=(s, e))

    item_list = item_list.select_related('project').order_by('invest_time')
    data = []
    for con in item_list:
        project = con.project
        id = con.id
        project_id = project.id
        project_name = project.name
        if con.is_futou:
            is_futou = "复投"
        else:
            is_futou = "首投"
        invest_time = con.invest_time
        invest_mobile = con.invest_mobile
        invest_amount = con.invest_amount
        invest_term = con.invest_term
        settle_amount = con.settle_amount
        return_amount = ''
        result = ''
        if con.state == '0':
            result = '是'
            return_amount = con.return_amount
        elif con.state == '2':
            result = '否'
        source = con.get_source_display()
        remark = con.remark
        data.append([id, project_id, project_name, is_futou, invest_time, invest_mobile, invest_amount, invest_term,
                     settle_amount,
                     result, return_amount, source, remark])
    w = Workbook()  # 创建一个工作簿
    ws = w.add_sheet(u'待审核记录')  # 创建一个工作表
    title_row = [u'记录ID', u'项目编号', u'项目名称', u'首投/复投', u'投资日期', u'提交手机号', u'投资金额', u'投资标期', u'预估消耗', u'审核状态',
                 u'返现金额', u'投资来源', u'备注']
    for i in range(len(title_row)):
        ws.write(0, i, title_row[i])
    row = len(data)
    style1 = easyxf(num_format_str='YY/MM/DD')
    for i in range(row):
        lis = data[i]
        col = len(lis)
        for j in range(col):
            if j == 4:
                ws.write(i + 1, j, lis[j], style1)
            else:
                ws.write(i + 1, j, lis[j])
    sio = StringIO()
    w.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=导出表格.xls'
    response.write(sio.getvalue())
    return response
