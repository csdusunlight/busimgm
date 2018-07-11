from django.shortcuts import render
from account.models import User,Group
from account.serializers import UserSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import  authenticate ,login , logout
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from django.contrib.auth.hashers import  make_password
import copy
from rest_framework import status
from utils.Exception import MyException
from django.http.response import JsonResponse
import time
from qiniu import Auth
from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt,csrf_protect



access_key = settings.QINIU_AK
secret_key = settings.QINIU_SK


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


class UserLoginAPIView(APIView):
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('uid')
        password = data.get('upwd')
        user = authenticate(username=username, password=password)
        if not user:
            raise MyException(detail="用戶名或密码输入错误",code=1)
        if user.is_active == False: #如果用戶被禁止登錄則爲false
            raise MyException(detail="用戶被禁止登录",code=2)
        login(request, user)
        returndata ={
                "code":0,
                "detail":"登录成功"}
        return Response(returndata)

class UserLogoutAPIView(APIView):
    authentication_classes = ()
    def post(self, request, *args, **kwargs):
        logout(request)
        returndata ={
                "code":0,
                "detail":"退出成功"}
        return Response(returndata)

@csrf_exempt
def check_user_login(request):
    user = request.user
    islogin = 1 if user.is_authenticated else 0
    data = {
        'permission':"no permission",
        'islogin':islogin
    }
    if islogin:
        permission = user.get_permission()
        data.update(username=user.uname, mobile=user.uid, qq=user.uqq,permission=permission)
    return JsonResponse(data)


class QiniuTokenView(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        q = Auth(access_key, secret_key)
        bucket_name = 'fulitianxia'
        key = 'daniu' + str(int(time.time() * 1000)) + '.jpg'
        token = q.upload_token(bucket_name, key, 3600, {})
        return Response({'token': token, 'code': 0, 'key': key})
