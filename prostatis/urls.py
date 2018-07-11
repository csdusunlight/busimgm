#coding:utf-8

from django.conf.urls import include, url

from django.urls import path
#from project import views as ProjectView
from account import views as AccountView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.views.generic.base import TemplateView
from project.views import ProjectDetail,FundApplyLogDetail,RefundApplyLogDetail,\
    InvoiceApplyLogDetail,ProjectInvestData
from prostatis.views import ProjectDayStatisList, DayStatisStatisList, UserDayStatisList, UserStatisList, statis_all

urlpatterns = [

    url(r'^project_day/$', ProjectDayStatisList.as_view()),
    url(r'^day/$', DayStatisStatisList.as_view()),
    url(r'^user_day/$', UserDayStatisList.as_view()),
    url(r'^user/$', UserStatisList.as_view()),
    url(r'^all/$', statis_all),
]
