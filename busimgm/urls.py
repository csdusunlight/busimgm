"""busimgm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url

from django.urls import path
#from project import views as ProjectView
from account import views as AccountView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from django.views.generic.base import TemplateView
from project.views import ProjectDetail,FundApplyLogDetail,RefundApplyLogDetail,\
    InvoiceApplyLogDetail,ProjectInvestData

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectDetail, base_name='project')
router.register(r'fundapplys', FundApplyLogDetail, base_name='fundapply')
router.register(r'refundapplys', RefundApplyLogDetail, base_name='refundapply')
router.register(r'invoiceapplys', InvoiceApplyLogDetail, base_name='invoiceapply')
router.register(r'projectinvestdata',ProjectInvestData,base_name='projectinvestdata')



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^login/$', csrf_exempt(AccountView.UserLoginAPIView.as_view())),
    url(r'^logout/$', csrf_exempt(AccountView.UserLogoutAPIView.as_view())),
    path('admin/', admin.site.urls),
    url(r'Project/', include(router.urls)),
    url(r'^User/$', AccountView.UserList.as_view()),
    path('statis/', include('prostatis.urls')),

    url(r'^check_user_login/$', AccountView.check_user_login),
    url(r'^get_upload_token/$', AccountView.QiniuTokenView.as_view()),
    url(r'^User/(?P<pk>[0-9]+)/$', AccountView.UserDetail.as_view(), kwargs={'partial':True}),

]
