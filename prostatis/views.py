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
from prostatis.serializers import DayStatisSerializer,ProjectStatisSerializer,UserStatisSerializer,UserDayStatisSerializer,ProjectDayStatisSerializer
import django_filters
from prostatis.Filters import ProjectDayStatisFilter,UserDayStatisFilter,DayStatisFilter,ProjectStatisFilter,UserStatisFilter
import datetime
from rest_framework.filters import SearchFilter, OrderingFilter
from prostatis.models import ProjectDayStatis,DayStatis,ProjectStatis,UserStatis,UserDayStatis


#Create your views here.
class ProjectDayStatisList(generics.ListCreateAPIView):
    queryset = ProjectDayStatis.objects.all()
    serializer_class = ProjectDayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectDayStatisFilter

class DayStatisStatisList(generics.ListCreateAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = DayStatisFilter

class UserDayStatisList(generics.ListCreateAPIView):
    queryset = UserDayStatis.objects.all()
    serializer_class = UserDayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = UserDayStatisFilter

class ProjectStatisList(generics.ListCreateAPIView):
    queryset = ProjectStatis.objects.all()
    serializer_class = ProjectStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectStatisFilter

class UserStatisList(generics.ListCreateAPIView):
    queryset = UserStatis.objects.all()
    serializer_class = UserStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = UserStatisFilter

class ProStatis(viewsets.ViewSet):
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

        data={}
        for item in row:
            print(item)
            data['onlineprojectnum'] = item[0]
            data['currenttosettlenum'] = item[1]
            data['currenttosettlepronum'] = item[2]
            data['currenttoconsumenum'] = item[3]
            data['currenttoconsumepronum'] = item[4]
        returndict['data']=data
        returndict['code']=0
        return Response(returndict)

