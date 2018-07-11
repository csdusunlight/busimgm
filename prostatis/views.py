from django.http import JsonResponse
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
from prostatis.serializers import DayStatisSerializer,UserStatisSerializer,UserDayStatisSerializer,ProjectDayStatisSerializer
import django_filters
from prostatis.Filters import ProjectDayStatisFilter,UserDayStatisFilter,DayStatisFilter,UserStatisFilter
import datetime
from rest_framework.filters import SearchFilter, OrderingFilter
from prostatis.models import ProjectDayStatis,DayStatis,UserStatis,UserDayStatis


#Create your views here.
class ProjectDayStatisList(generics.ListAPIView):
    queryset = ProjectDayStatis.objects.all()
    serializer_class = ProjectDayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectDayStatisFilter

class DayStatisStatisList(generics.ListAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = DayStatisFilter

class UserDayStatisList(generics.ListAPIView):
    queryset = UserDayStatis.objects.all()
    serializer_class = UserDayStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_class = UserDayStatisFilter


class UserStatisList(generics.ListAPIView):
    queryset = UserStatis.objects.all()
    serializer_class = UserStatisSerializer
    pagination_class = MyPageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = UserStatisFilter

def statis_all(request):
    '''　数据总览:在线项目数　　 待结算金额 待结算项目数 待消耗金额 待消耗项目数　　正负数关系'''
    cursor = connection.cursor()
    cursor.execute("select 	sum(case when state='1' then 1 else 0 end) ,\
                            sum(case when consume-settle>0 then 1 else 0 end ),\
                            sum(case when consume-settle>0 then consume -settle else 0 end),\
                            sum(case when consume-settle<0 then 1 else 0 end ),\
                            sum(case when consume-settle<0 then settle-consume else 0 end )\
                            from project_project")
    # cursor.execute("select 	sum(case when state='1' then 1 else 0 end) ,\
    #                         sum(case when consume-settle<0 then 1 else 0 end ),\
    #                         sum(case when consume-settle<0 then consume -settle else settle-consume end),\
    #                         sum(case when consume-settle>0 then 1 else 0 end ),\
    # 			            sum(case when consume-settle>0 then settle-consume else consume-settle end )\
    #                         from project_project")

    row = cursor.fetchall()
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
    return JsonResponse(returndict)

