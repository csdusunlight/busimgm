from django.shortcuts import render
from prostatis.models import DayStatis
from prostatis.serializers import DayStatisSerializer
from utils.Mypagination import MyPageNumberPagination
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route,action
from django.db import connection, transaction
from rest_framework.response import Response
from project.models import  ProjectInvestDataModel
from project.serializers import ProjectInvestDataSerializer
import django_filters
import datetime


#Create your views here.
class DayStatisList(generics.ListCreateAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination

class ProjectDetailList(generics.ListCreateAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination


class ProStatis(viewsets.ModelViewSet):
    queryset = ProjectInvestDataModel.objects.all()
    serializer_class = ProjectInvestDataSerializer
    @action(methods=['get'],detail=False)
    def get_date(self, request, pk=None,*args,**kwargs):
        '''　项目详情:到项目详情　　单个项目的每天信息　日期   当前总待收   预估利润    昨日结算金额  '''
        cursor = connection.cursor()
        cursor.execute("select  a.project_id, \
                                a.source,\
                                a.audit_time, \
                                b.consume-b.settle,\
                                a.source,\
		                        a.settle_amount,\
		                        sum(a.settle_amount) as sumofsettle,\
		                        sum(a.return_amount) as sumofret,\
		                        b.paccountype as accounttype,\
		                        sum(case b.paccountype when '0' then a.settle_amount*0.94 -a.return_amount  else  a.settle_amount -a.return_amount end )\
                        from project_projectinvestdatamodel as a\
                        left join project_project as b on b.id = a.project_id\
                        group by a.project_id, a.audit_time\
                        order by a.project_id, a.audit_time")
        row = cursor.fetchall()
        print(row)
        returndict={}

       # row[0]是今天的
       # row[1]是昨天的
        for item in row:
            print(item)
            returndict['date']=item[2]
            print(item[0])
            print(item[3])
            returndict['currenttopay']=item[1]
            returndict['preprofit']=item[7]


        return Response(returndict)

    @action(methods=['get'], detail=False)
    def get_date1(self, request, pk=None, *args, **kwargs):
        '''　数据总览:在线项目数　　 待结算金额 待结算项目数 待消耗金额 待消耗项目数　　正负数关系'''
        cursor = connection.cursor()
        cursor.execute("select 	sum(case when state='1' then 1 else 0 end) ,\
                                sum(case when consume-settle<0 then 1 else 0 end ),\
                                sum(case when consume-settle<0 then consume -settle else settle-consume end),\
                                sum(case when consume-settle>0 then 1 else 0 end ),\
        			            sum(case when consume-settle>0 then settle-consume else consume-settle end )\
                                from project_project")

        row = cursor.fetchall()
        print(row)
        returndict={}
        for item in row:
            print(item)
            returndict['onlineprojectnum'] = item[0]
            returndict['currenttosettlenum'] = item[1]
            returndict['currenttosettlepronum'] = item[2]
            returndict['currenttoconsumenum'] = item[3]
            returndict['currenttoconsumepronum'] = item[4]

        return Response(returndict)


    @action(methods=['get'], detail=False)
    def get_date2(self, request, pk=None, *args, **kwargs):
        '''　日期 新增项目数 结项项目数 有效项目数（有交单的） 投资人数 投资金额 消耗费用 返现投资人数 返现投资金额 返现费用'''
        cursor = connection.cursor()
        cursor.execute("select *\
    from\
    (\
        select lanched_apply_date as 'A1', count(*) as 'B1' from project_project group by lanched_apply_date\
    )t1\
    left join\
    (\
        select count(*) as 'B2', concluded_audit_date as 'A2'\
        from project_project\
        group by concluded_audit_date\
    )t2 on t1.lanched_apply_date = t2.concluded_audit_date\
    left join\
    (\
	    select lanched_apply_date as 'A3', count(distinct project_id) as 'B3'\
        from project_projectinvestdatamodel\
        left join project_project\
        on project_projectinvestdatamodel.project_id = project_project.id\
        group by lanched_apply_date\
    )t3  on t2.concluded_audit_date=t3.lanched_apply_date\
    left join\
    (\
	    select invest_time as 'A4',count(distinct invest_mobile) as 'B4', sum(invest_amount) as 'B5'\
        from project_projectinvestdatamodel\
        group by invest_time\
    )t4  on t3.lanched_apply_date=t4.invest_time\
    left join\
    (\
        select audit_time as 'A5',count(distinct invest_mobile) as 'B6',\
                sum(invest_amount) as 'B7',\
                sum(return_amount) as 'B8'\
        from project_projectinvestdatamodel\
        where return_amount is not null and return_amount >= 0\
        group by audit_time\
    )t5  on t4.invest_time=t5.audit_time ")

        # cursor.execute("select B1,B2 from (select lanched_apply_date, count( *) as B1 from project_project group by lanched_apply_date) t1\
        # left join (select count(*) as B2, concluded_audit_date from project_project group by concluded_audit_date) t2 \
        # on t1.lanched_apply_date = t2.concluded_audit_date")
        row = cursor.fetchall()
        print(row)
        returndict={}
        returndict['code']=0
        returndict['result'] = row

        return Response(returndict)




