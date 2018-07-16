from project.models import OperatorLog
import datetime
from django.db import models
from project.models import Project,ProjectInvestDataModel




def strformat(ouser,obj,otype,request):#对修改和删除的对象的具体返回格式
    #传入
    if otype=='1':#1是修改,原来是什么，现在是什么
        if isinstance(obj,Project):
            afterdata = request.data
            beforedata = [obj.__getattribute__(i) for i in afterdata]
            strtest = "项目申请"+"{} "*len(afterdata)*2+"修改为" +"{} "*len(afterdata)
            result = strtest.format(*afterdata,*beforedata,*afterdata.values())
            return result
            #"九九          2018-07-16     修改         项目申请-对公对私：对私改为对公；平台名称：123改为456"
        elif isinstance(obj,ProjectInvestDataModel):
            afterdata = request.data
            beforedata = [obj.__getattribute__(i) for i in afterdata]
            strtest = "投资数据"+"{} "*len(afterdata)*2+"修改为" +"{} "*len(afterdata)
            result = strtest.format(*afterdata,*beforedata,*afterdata.values())
            return result


    elif otype=='0':#0是删除
        if isinstance(obj, Project):
            return "删除　项目申请　%s" % (ouser.uid,datetime.datetime.today().strftime("%d/%m/%y"),repr(obj))
        elif isinstance(obj,ProjectInvestDataModel):
            return "删除　投资数据　%s" % (ouser.uid, datetime.datetime.today().strftime("%d/%m/%y"),repr(obj))


def write_to_log(ouser,obj,otype,request):
    #obj对应的file,otype是operator的对应的操作type
    if isinstance(obj,models.Model):
        oobj = strformat(ouser,obj,otype,request)
    else:
        oobj=obj
    OperatorLog.objects.create(otime=datetime.datetime.now(), oman=ouser, oobj=oobj, otype=otype)