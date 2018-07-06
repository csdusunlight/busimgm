from django.shortcuts import render
from prostatis.models import DayStatis
from prostatis.serializers import DayStatisSerializer
from utils.Mypagination import MyPageNumberPagination
from rest_framework import generics
import django_filters
import datetime


# Create your views here.
class DayStatisList(generics.ListCreateAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination

class ProjectDetailList(generics.ListCreateAPIView):
    queryset = DayStatis.objects.all()
    serializer_class = DayStatisSerializer
    pagination_class = MyPageNumberPagination



