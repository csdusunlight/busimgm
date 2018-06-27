from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

ACCOUNT_TYPE = {
    ('0','对公'),
    ('1','对私'),
}
SETTLE_METHOD = {
    ('0','预付款'),
    ('1','待付款'),
}
AUDIT_STATE = (
    ('0', u'审核通过'),
    ('1', u'待审核'),
    ('2', u'审核未通过'),
)
class Project(models):
    pid =models.CharField("项目编号", max_length=11, unique=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,verbose_name="用户")
    pname = models.CharField("项目名字", max_length=20)
    company= models.CharField("甲方公司名称", max_length=20)
    ppname= models.CharField("平台名字", max_length=20)
    paccountype= models.CharField("账户类型",choices=ACCOUNT_TYPE,max_length=2)
    psettlemethod= models.CharField("结算方式",choices=SETTLE_METHOD, max_length=2)
    psettledetail= models.CharField("结算详情", max_length=200)
    psigncompany= models.CharField("签约公司", max_length=50)
    pcoperatedetail= models.CharField("合作详情", max_length=200)
    record= models.CharField("备注", max_length=200)
    state= models.CharField("项目状态",choices=AUDIT_STATE, max_length=20)
    psettlenum= models.CharField("结算金额", max_length=20)
    psettlereason= models.CharField("结项原因", max_length=20)
    auditstate= models.CharField("项目审核状态",choices=AUDIT_STATE, max_length=20)
    pbuildate= models.DateField("立项日期",default=timezone.now)
    penddate= models.DateField("结项日期",default=timezone.now,blank=True,null=True)
    pauditdate= models.DateField("审核日期",default=timezone.now,blank=True,null=True)

