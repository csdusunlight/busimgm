from django.shortcuts import render
from account.models import User,Group
from account.serializers import UserSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django.contrib.auth.hashers import  make_password
import copy
from rest_framework import status





class UserList(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ('uname')
    search_fields = ('ugroup')
    ordering = ('uname')


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,*args,**kwargs):
        #传入主键，返回
        userpk = kwargs['pk']
        user = User.objects.get(pk=userpk)
        return Response(user.uid)


    #，传入对应的user id如果是管理员的话，可以直接修改，如果是user自己的话，就只能修改自己的,所以要校对upk
    #is_staff ,接口的权限仍然有对应的划分
    #接口功能，更改密码，更改组名，更改qq,更改离职时间，更改加入时间，更改is_avtive字段来禁止登录,更改权限
    #如果是管理员就不需要验证密码，直接更改，如果是用户，那就需要验证密码
    #将密码独立出来，而其他字段就统一partial update 。
    def put(self, request, *args, **kwargs):
            #可以执行条件
        #首先判断用户名是否
        upk = kwargs['pk']
        password = make_password(request.data['password'])
        aimdata = copy.deepcopy(request.data)
        print(aimdata)
        aimdata['password']=password
        print(aimdata)
        oldobj = User.objects.get(pk=upk)
        userserializer = UserSerializer(oldobj,data=aimdata,partial=True)
        if userserializer.is_valid():
            userserializer.save()

        #如果创建成功，返回对应id的对应url
        returndata = {
                "desc":"user add",
                "data":{
                            "upk": upk
                        },
                "code":200,
                "error":0,
                "detail":"add success"
        }
        return Response(returndata,status=status.HTTP_200_OK)
