from project.models import OperatorLog
import datetime
from django.db import models
from project.models import Project,ProjectInvestDataModel
from rest_framework.filters import OrderingFilter



def strformat(ouser,obj,otype,request):#对修改和删除的对象的具体返回格式
    #传入
    if otype=='1':#1是修改,原来是什么，现在是什么
        if isinstance(obj,Project):
            getdata = request.data #待更新的集合
            toupdatedata = [(i,obj.__getattribute__(i),getdata[i]) for i in getdata if getdata[i]!=obj.__getattribute__(i)]
            print(toupdatedata)
            restr="项目申请:"
            for i in toupdatedata:
                stritem = "{}修改前为{},修改后为{};"
                restr += stritem.format(*i)
            print(restr)
            return restr
        elif isinstance(obj,ProjectInvestDataModel):
            afterdata = request.data
            beforedata = [obj.__getattribute__(i) for i in afterdata]
            strtest = "投资数据"+"{} "*len(afterdata)*2+"修改为" +"{} "*len(afterdata)
            result = strtest.format(*afterdata,*beforedata,*afterdata.values())
            return result

    elif otype=='0':#0是删除
        if isinstance(obj, Project):
            return "删除　项目申请　{}".format(repr(obj))
        elif isinstance(obj,ProjectInvestDataModel):
            return "删除　投资数据　{}".format(repr(obj))


def write_to_log(ouser,obj,otype,request):
    #obj对应的file,otype是operator的对应的操作type
    if isinstance(obj,models.Model):
        oobj = strformat(ouser,obj,otype,request)
    else:
        oobj=obj
    OperatorLog.objects.create(otime=datetime.datetime.now(), oman=ouser, oobj=oobj, otype=otype)