from project.models import OperatorLog
import datetime
from django.db import models


def write_to_log(ouser,obj,otype):
    #obj对应的file,otype是operator的对应的操作type
    if isinstance(obj,models.Model):
        oobj = repr(obj)
    else:
        oobj=obj
    OperatorLog.objects.create(otime=datetime.datetime.now(), oman=ouser, oobj=oobj, otype=otype)