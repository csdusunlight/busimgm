from io import BytesIO

from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from project.models import Project,FundApplyLog,RefundApplyLog,InvoiceApplyLog,OperatorLog,ProjectInvestDataModel
from project.serializers import ProjectSerializer,FundApplyLogSerializer,\
    RefundApplyLogSerializer,InvoiceApplyLogSerializer,FundApplyLogListSerializer,\
    RefundApplyLogListSerializer,InvoiceApplyLogListSerializer,OperatorLogSerializer,ProjectInvestDataSerializer
from project.Filters import ProjectFilter,FundApplyLogFilter,RefundApplyLogFilter,\
    InvoiceApplyLogFilter,OperatorLogFilter,ProjectInvestDataFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from account.permissions import IsAllowedToUse,IsOwnerOrStaff

from django.views.decorators.clickjacking import xframe_options_sameorigin



import django_filters
from django.http.response import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import xlrd
import logging
from django.db import transaction
from decimal import Decimal

from xlwt.Workbook import Workbook
from xlwt.Style import easyxf
import traceback
import datetime
from project.models import DBlock
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route,action
from rest_framework import viewsets
from django.core.cache import cache
from utils.Mypagination import MyPageNumberPagination
#import django.core.cache
import time
logger = logging.getLogger('busimgm')
ts = lambda :time.time
class ProjectDetail(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectFilter
    ordering_fields = ('name')
    search_fields = ('name')
    ordering=('lanched_apply_date','concluded_audit_date')
    permission_classes =(IsAllowedToUse,)
    '''三个操作分别是修改，删除，结项申请，都是商务人员发起的'''
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret={}
        ret['code']=0
        return Response(ret)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(contact=user,lanched_apply_date=datetime.date.today())
        data = serializer.data
        serializer._data = {}
        serializer._data['code'] = 0
        serializer._data['data'] = data

    # @action(methods=['patch'],detail=True)
    # def is_deleted(self, request, pk=None,*args,**kwargs):
    #     '''删除
    #     字段仅仅限于is_delete'''
    #     judgeres = [True if i == "is_delete" else False for i in request.data ]
    #     if all(judgeres)==True:
    #         self.partial_update(request,*args,**kwargs)
    #     else:
    #         raise Exception("do not pass no need para!")
    #     res = {}
    #     res['code']=0
    #     return Response(res)

    @action(methods=['put'],detail=True)
    def is_altered(self, request, pk=None,*args,**kwargs):
        '''修改
        字段仅仅限于is_delete,进行中的项目要通知管理员'''
        aimpro = Project.objects.get(id=pk)
        #if aimpro.state in ['１',]:
        #    写操作日志，对应visit字段为False表示未读.而每个管理员登录后，都会更新当前的未读的操作日志有多少条，但这些操作日志是共享的
        self.partial_update(request,*args,**kwargs)
        res = {}
        res['code']=0
        return Response(res)

    @action(methods=['patch'],detail=True)
    def is_concluded(self, request, pk=None,*args,**kwargs):
        """结项
        字段应该是结算金额settle，结项原因psettlereason"""
        judgeres = [True if i in ['settle','psettlereason'] else False for i in request.data ]
        if  all(judgeres)==True:
            self.partial_update(request,*args,**kwargs)
        else:
            raise Exception("do not pass no need para!")
        res = {}
        res['code'] =0
        return Response(res)

    @action(methods=['post'],detail=True)
    def lanchedpro_approved(self, request, pk=None,*args,**kwargs):
        """立项审核通过"""
        aimpro = Project.objects.get(id=pk)
        aimpro.audituser=request.user
        aimpro.state='1'
        aimpro.lanched_audit_date=  datetime.date.today()
        aimpro.save(update_fields=['audituser','state','lanched_apply_date'])
        res = {}
        res['code'] = 0
        return Response(res)


    @action(methods=['post'],detail=True)
    def lanchedpro_rejected(self, request, pk=None,*args,**kwargs):
        """立项审核拒绝"""
        lanched_refused_reason=request.data['reason']
        aimpro = Project.objects.get(id=pk)
        aimpro.audituser=request.user
        aimpro.state='2'
        aimpro.lanched_audit_date =  datetime.date.today()

        aimpro.lanched_refused_reason = lanched_refused_reason
        aimpro.save()
        res = {}
        res['code'] = 0
        return Response(res)

    @action(methods=['post'], detail=True)
    def concludedpro_apply(self, request, pk=None, *args, **kwargs):
        """结项申请,有结算金额和结算原因"""
        settle = request.POST.get("settle")
        psettlereason = request.POST.get("reason")
        aimpro = Project.objects.get(id=pk)
        aimpro.audituser = request.user
        aimpro.state = "4" #"结项待审核"
        aimpro.settle = settle
        aimpro.psettlereason = psettlereason
        aimpro.concluded_apply_date = datetime.date.today()
        aimpro.save()
        res = {}
        res['code'] = 0
        return Response(res)


    @action(methods=['post'],detail=True)
    def concludedpro_approved(self, request, pk=None,*args,**kwargs):
        """结项审核通过,"""
        aimpro = Project.objects.get(id=pk)
        aimpro.audituser=request.user
        aimpro.state='5'
        aimpro.concluded_audit_date = datetime.date.today()
        aimpro.save()
        res = {}
        res['code'] = 0
        return Response(res)

    @action(methods=['post'],detail=True)
    def concludedpro_rejected(self, request, pk=None,*args,**kwargs):
        """结项审核拒绝"""
        conclued_refused_reason=request.data['reason']
        aimpro = Project.objects.get(id=pk)
        aimpro.audituser=request.user
        aimpro.state='6'
        aimpro.concluded_audit_date = datetime.date.today()
        aimpro.conclued_refused_reason = conclued_refused_reason
        aimpro.save()
        res = {}
        res['code'] = 0
        return Response(res)

class FundApplyLogDetail(viewsets.ModelViewSet):
    queryset = FundApplyLog.objects.all()
    serializer_class = FundApplyLogSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = FundApplyLogFilter
    #permission_classes =

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret={}
        ret['code']=0
        return Response(ret)

    def get_serializer(self, *args, **kwargs):
        print("1111")

        if self.request.method == "GET":
            serializer_class = FundApplyLogListSerializer
            print(serializer_class)
        elif self.request.method in ["POST","PUT","PATCH"]:
            serializer_class = self.get_serializer_class()
            print(serializer_class)

        kwargs['context'] = self.get_serializer_context()
        print(serializer_class)
        return serializer_class(*args, **kwargs)



    '''三个操作分别是修改，删除，结项申请，都是商务人员发起的'''
    def perform_create(self, serializer):
        user= self.request.user
        serializer.save(apply_man=user,state='0')
        data = serializer.data
        serializer._data = {}
        serializer._data['code'] = 0
        serializer._data['data'] = data

    @action(methods=['patch'],detail=True)
    def is_deleted(self, request, pk=None,*args,**kwargs):
        '''删除
        字段仅仅限于is_delete'''
        judgeres = [True if i == "is_delete" else False for i in request.data ]
        if all(judgeres)==True:
            self.partial_update(request,*args,**kwargs)
        else:
            raise Exception("do not pass no need para!")
        res = {}
        res['code']=0
        return Response(res)

    @action(methods=['put'],detail=True)
    def is_altered(self, request, pk=None,*args,**kwargs):
        '''修改
        字段仅仅限于is_delete'''
        self.partial_update(request,*args,**kwargs)
        res = {}
        res['code']=0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_approved(self, request, pk=None,*args,**kwargs):
        """审核通过"""
        aimfund = FundApplyLog.objects.get(id=pk)
        aimfund.audit_man=request.user
        aimfund.state='1'
        aimfund.audit_date = datetime.date.today()
        aimfund.save(update_fields=['audituser','state','audit_date'])

        #同时把对应的project的settle加上
        aimpro = aimfund.project
        aimpro.settle+=aimfund.fund_rec
        aimpro.save(update_fields=['settle'])

        res = {}
        res['code'] = 0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_rejected(self, request, pk=None,*args,**kwargs):
        """立项审核拒绝"""
        reason=request.data['reason']
        aimfund = FundApplyLog.objects.get(id=pk)
        aimfund.audit_man=request.user
        aimfund.state='2'
        aimfund.audit_date =  datetime.date.today()

        aimfund.audit_refused_reason = reason
        aimfund.save(update_fields=['audituser','state','audit_refused_reason','audit_date'])
        res = {}
        res['code'] = 0
        return Response(res)


class RefundApplyLogDetail(viewsets.ModelViewSet):
    queryset = RefundApplyLog.objects.all()
    serializer_class = RefundApplyLogSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = RefundApplyLogFilter
    #permission_classes =
    '''三个操作分别是修改，删除，结项申请，都是商务人员发起的'''

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret={}
        ret['code']=0
        return Response(ret)

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "GET":
            serializer_class = RefundApplyLogListSerializer
            print(serializer_class)
        elif self.request.method in ["POST","PUT","PATCH"]:
            serializer_class = self.get_serializer_class()
            print(serializer_class)

        kwargs['context'] = self.get_serializer_context()
        print(serializer_class)
        return serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(apply_man=user,state='0')
        data = serializer.data
        serializer._data = {}
        serializer._data['code'] = 0
        serializer._data['data'] = data

    @action(methods=['patch'],detail=True)
    def is_deleted(self, request, pk=None,*args,**kwargs):
        '''删除
        字段仅仅限于is_delete'''
        judgeres = [True if i == "is_delete" else False for i in request.data ]
        if all(judgeres)==True:
            self.partial_update(request,*args,**kwargs)
        else:
            raise Exception("do not pass no need para!")
        res = {}
        res['code']=0
        return Response(res)

    @action(methods=['put'],detail=True)
    def is_altered(self, request, pk=None,*args,**kwargs):
        '''修改
        字段仅仅限于is_delete'''
        self.partial_update(request,*args,**kwargs)
        res = {}
        res['code']=0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_approved(self, request, pk=None,*args,**kwargs):
        """审核通过"""
        aimrefund = RefundApplyLog.objects.get(id=pk)
        aimrefund.audit_man=request.user
        aimrefund.state='1'
        aimrefund.audit_date = datetime.date.today()
        aimrefund.save(update_fields=['audituser','state','audit_date'])
        aimpro = aimrefund.project
        if aimrefund.is_invoice=="1":
            aimpro.settle -= aimrefund.refund_rec
        elif aimrefund.is_invoice=="0":
            aimpro.settle -= aimrefund.refund_rec
            aimpro.invoicenum -= aimrefund.refund_rec
        aimpro.save(update_fields=['settle','invoicenum'])

        res = {}
        res['code'] = 0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_rejected(self, request, pk=None,*args,**kwargs):
        """立项审核拒绝"""
        reason=request.data['reason']
        aimrefend = RefundApplyLog.objects.get(id=pk)
        aimrefend.audit_man=request.user
        aimrefend.state='2'
        aimrefend.audit_date =  datetime.date.today()

        aimrefend.audit_refused_reason = reason
        aimrefend.save()
        res = {}
        res['code'] = 0
        return Response(res)

class InvoiceApplyLogDetail(viewsets.ModelViewSet):
    queryset = InvoiceApplyLog.objects.all()
    serializer_class = InvoiceApplyLogSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = InvoiceApplyLogFilter
    '''三个操作分别是修改，删除，结项申请，都是商务人员发起的'''

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret={}
        ret['code']=0
        return Response(ret)

    def get_serializer(self, *args, **kwargs):
        if self.request.method == "GET":
            serializer_class = InvoiceApplyLogListSerializer
            print(serializer_class)
        elif self.request.method in ["POST","PUT","PATCH"]:
            serializer_class = self.get_serializer_class()
            print(serializer_class)

        kwargs['context'] = self.get_serializer_context()
        print(serializer_class)
        return serializer_class(*args, **kwargs)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(apply_man=user,state='0')
        data = serializer.data
        serializer._data = {}
        serializer._data['code'] = 0
        serializer._data['data'] = data

    @action(methods=['patch'],detail=True)
    def is_deleted(self, request, pk=None,*args,**kwargs):
        '''删除
        字段仅仅限于is_delete'''
        judgeres = [True if i == "is_delete" else False for i in request.data ]
        if all(judgeres)==True:
            self.partial_update(request,*args,**kwargs)
        else:
            raise Exception("do not pass no need para!")
        res = {}
        res['code']=0
        return Response(res)

    @action(methods=['put'],detail=True)
    def is_altered(self, request, pk=None,*args,**kwargs):
        '''修改
        字段仅仅限于is_delete'''
        self.partial_update(request,*args,**kwargs)
        res = {}
        res['code']=0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_approved(self, request, pk=None,*args,**kwargs):
        """审核通过"""
        aiminvoice = InvoiceApplyLog.objects.get(id=pk)
        aiminvoice.audit_man=request.user
        aiminvoice.state='1'
        aiminvoice.audit_date = datetime.date.today()
        aiminvoice.save(update_fields=['audituser','state','audit_date'])
        aimpro = aiminvoice.project
        aimpro.invoicenum = aiminvoice.invoice_num
        aimpro.save(update_fields=['invoicenum'])
        res = {}
        res['code'] = 0
        return Response(res)


    @action(methods=['post'],detail=True)
    def apply_rejected(self, request, pk=None,*args,**kwargs):
        """立项审核拒绝"""
        reason=request.data['reason']
        aiminvoice =  InvoiceApplyLog.objects.get(id=pk)
        aiminvoice.audit_man=request.user
        aiminvoice.state='2'
        aiminvoice.audit_date =  datetime.date.today()

        aiminvoice.audit_refused_reason = reason
        aiminvoice.save(update_fields=['audituser','state','audit_refused_reason','audit_date'])
        res = {}
        res['code'] = 0
        return Response(res)

class OperatorLogDetail(viewsets.ModelViewSet):
    queryset = OperatorLog.objects.all()
    serializer_class = OperatorLogSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = OperatorLogFilter


from django.views.decorators.clickjacking import xframe_options_exempt

# @method_decorator(xframe_options_exempt, name='export_investdata_excel')
class ProjectInvestData(viewsets.ModelViewSet):
    queryset = ProjectInvestDataModel.objects.all()
    serializer_class = ProjectInvestDataSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectInvestDataFilter
    permission_classes = ()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        ret={}
        ret['code']=0
        return Response(ret)

    def perform_update(self, serializer):
        if self.request.data.get('state'):
            serializer.save(audit_time=datetime.datetime.now())
        else:
            serializer.save()

    @action(methods=['post'], detail=True)
    def import_apply_approved(self,request,pk=None,*args,**kwargs):
        aiminvestrecord=ProjectInvestDataModel.objects.get(id=pk)
        source = request.data.get('source')
        return_amount = request.data.get('return_amount')
        invest_mobile = request.data.get('invest_mobile')
        aiminvestrecord.audit_time= datetime.date.today()
        aiminvestrecord.source = source
        aiminvestrecord.return_amount = return_amount
        aiminvestrecord.invest_mobile = invest_mobile
        aiminvestrecord.state='1'
        aiminvestrecord.save(update_fields=['audit_time','state','source','invest_mobile','return_amount'])
        resultdict={}
        resultdict['code']=0
        return Response(resultdict)

    @action(methods=['post'], detail=True)
    def import_apply_rejected(self, request, pk=None, *args, **kwargs):
        aiminvestrecord = ProjectInvestDataModel.objects.get(id=pk)
        aiminvestrecord.audit_time = datetime.date.today()
        aiminvestrecord.state = '2'
        aiminvestrecord.save(update_fields=['audit_time', 'state'])


    @action(methods=['get'],detail=False)
    def export_investdata_excel(self,request):
        item_list = self.filter_queryset(self.get_queryset())
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
        sio = BytesIO()
        w.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=导出表格.xls'
        response.write(sio.getvalue())
        return response

    @action(methods=['post'], detail=False)
    def import_audit_projectdata_excel_except(self,request):
        admin_user = request.user
        ret = {'code': -1}
        file = request.FILES.get('file')
        #     print file.name
        aftername=time.time()
        filename = "./files/"+str(int(aftername*1000))
        with open(filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        data = xlrd.open_workbook(filename)
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
            ret['msg'] = e.__str__()
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
                event = ProjectInvestDataModel.objects.get(id=id)
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
                event.save()
                suc_num += 1
            ret['code'] = 0
        except Exception as e:
            exstr = traceback.format_exc()
            logger.info(exstr)
            ret['code'] = 1
            ret['msg'] = e.__str__()
        ret['num'] = suc_num
        return JsonResponse(ret)



    @action(methods=['post'], detail=False)
    def import_audit_projectdata_excel(self,request):
        admin_user = request.user
        ret = {'code': -1}
        # print(dir(request))
        file = request.FILES.get('file')
        aftername=time.time()
        filename = "./files/"+str(int(aftername*1000))
        with open(filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        data = xlrd.open_workbook(filename)
        table = data.sheets()[0]
        print(table)
        nrows = table.nrows
        ncols = table.ncols
        if ncols != 13:
            ret['msg'] = "文件格式与模板不符，请下载最新模板填写！"
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
                    raise Exception("手机号必须是11位，请修改后重新提交。")
                if row[9] == "是":
                    result = True
                    temp['state'] = '1'
                elif row[9] == "否":
                    result = False
                    temp['state'] = '0'
                else:
                    raise Exception("审核结果必须为是或否。")

                if row[10]:
                    return_amount = Decimal(row[10])
                    if return_amount > consume:
                        raise Exception("返现金额不能大于结算金额，请检查表格")
                elif result:
                    raise Exception("审核结果为是时，返现金额不能为空或零。")
                else:
                    return_amount = 0

                if row[11] == "网站":
                    source = 'site'
                elif row[11] == "渠道":
                    source = 'channel'
                else:
                    raise Exception("必须为网站或渠道。")
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
            print(e)
            #             traceback.print_exc()
            ret['msg'] = e.__str__()
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
                print(id)
                event = ProjectInvestDataModel.objects.get(id=id)
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
                event.save()
                suc_num += 1
            ret['code'] = 0
        except Exception as e:
            exstr = traceback.format_exc()
            logger.info(exstr)
            ret['code'] = 1
            ret['msg'] = e.__str__()
        ret['num'] = suc_num
        return JsonResponse(ret)


    @action(methods=['post'], detail=False)
    def import_projectdata_excel(self,request):
        admin_user = request.user
        ret = {}
        file = request.FILES.get('file')
        # aftername＝time.time()
        filename = "./files/" +"1"
        with open(filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        data = xlrd.open_workbook(filename)
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
                    print(value)

                    if j == 0:
                        id = int(value)
                        print(id)
                        project = Project.objects.get(id=id)
                        temp.append(id)
                    elif j == 2:
                        value = str(value).strip()
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
                            time2 = xlrd.xldate.xldate_as_datetime(value, 0)
                            temp.append(time2)
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
                    print(dup)
                    if tid in dup:
                        if temp[4] in dup[tid]:
                            continue
                        else:
                            dup[tid].append(temp[4])
                    else:
                        dup[tid] = [temp[4], ]

                if tid in rtable:
                    rtable[tid].append(temp)
                else:
                    rtable[tid] = [temp, ]
        except Exception as e:

            logger.info(e)
            #             traceback.print_exc()
            ret['msg'] = e.__str__()
            return JsonResponse(ret)
        ####开始去重
        investdata_list = []
        duplicate_mobile_list = []
        try:

            with cache.lock('investdata_first', timeout=2):
                # db_key = DBlock.objects.select_for_update().get(index='investdata')
                for id, values in rtable.items():
                    print(id)
                    temp = ProjectInvestDataModel.objects.filter(project_id=id).values('invest_mobile')
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
                            obj = ProjectInvestDataModel(project_id=pid, invest_mobile=mob, settle_amount=settle,
                                                    invest_amount=amount, invest_term=term, invest_time=time,
                                                    state='0', remark=remark, source=source, is_futou=is_futou)
                            investdata_list.append(obj)
                ProjectInvestDataModel.objects.bulk_create(investdata_list)
        except Exception as e:
            logger.info(e)
            #             traceback.print_exc()
            ret['msg'] = e.__str__()
            return JsonResponse(ret)
        succ_num = len(investdata_list)
        duplic_num2 = len(duplicate_mobile_list)
        duplic_num1 = nrows - 1 - succ_num - duplic_num2
        duplic_mobile_list_str = u'，'.join(duplicate_mobile_list)
        ret.update(num=succ_num, dup1=duplic_num1, dup2=duplic_num2, anum=nrows - 1,
                   dupstr=duplic_mobile_list_str)
        returndict ={}
        returndict['data']=ret
        returndict['code']=0
        return JsonResponse(ret)



