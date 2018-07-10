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
                                b.consume-b.settle,\
                                a.source,\
                                a.audit_time,\
		                        a.settle_amount,\
		                        sum(a.settle_amount) as sumofsettle,\
		                        sum(a.return_amount) as sumofret,\
		                        b.paccountype as accounttype,\
		                        sum(case b.paccountype when '0' then a.settle_amount*0.94 -a.return_amount  else  a.settle_amount -a.return_amount end )\
                        from project_projectinvestdatamodel as a\
                        left join project_project as b on b.id = a.project_id\
                        group by a.project_id, a.audit_time")
        row = cursor.fetchall()
        returndict={}
        for item in row:
            returndict['date']=item[2]
            returndict['currenttopay']=item[1]
            returndict['preprofit']=item[7]


        return Response(returndict)



