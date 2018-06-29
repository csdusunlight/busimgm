from django.db import models
from account.models import User
from django.utils import timezone
import datetime

# Create your models here.

ACCOUNT_TYPE = {
    ('0','对公'),
    ('1','对私'),
}
SETTLE_STATE=(
    ('advance', "预付款"),
    ('later', "后付款"),
    ('daily', "日结"),
)
AUDIT_STATE = (
    ('1', u'审核通过'),
    ('0', u'待审核'),
    ('2', u'审核未通过'),
)
PAUDIT_STATE = (
    ('0', u'待审核'),
    ('2', u'审核未通过'),
    ('3', u'进行中'),
    ('4', u'结项中'),
    ('5', u'已结项'),
    ('6', u'结项失败'),

)
SUB_TYPE = (
    ('1', u'首投'),
    ('2', u'复投'),
)

SOURCE=(
    ('site', "网站"),
    ('channel', "渠道"),
)

OTYPE = (
    ('0', '删除'),
    ('1', '修改'),
    ('2', '导入'),
)


class Project(models.Model):
    pid =models.CharField("项目编号", max_length=11, unique=True)
    contact=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="商务对接人",related_name="contact")
    audituser=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="auditman",verbose_name="审核人",blank=True,null=True)
    name = models.CharField("项目名字", max_length=50)
    company= models.CharField("甲方公司名称", max_length=20)
    platname= models.CharField("平台名字", max_length=20)
    paccountype= models.CharField("账户类型",choices=ACCOUNT_TYPE,max_length=2)
    settleway= models.CharField("结算方式",choices=SETTLE_STATE, max_length=2)
    settle_detail= models.CharField("结算详情", max_length=30)
    contract_company = models.CharField("签约公司", max_length=50)
    pcoperatedetail= models.CharField("合作详情", max_length=200)
    remark= models.CharField("备注", max_length=200,blank=True,null=True)
    state= models.CharField("项目状态",choices=PAUDIT_STATE, max_length=20)
    settle = models.DecimalField("结算费用", max_digits=10, decimal_places=2, default=0)
    psettlereason= models.CharField("结项原因", max_length=20,null=True)
    auditstate= models.CharField("项目审核状态",choices=AUDIT_STATE, max_length=20)
    time= models.DateField("立项日期",default=datetime.date.today)
    finish_time = models.DateField("结项日期", blank=True,null=True)
    consume = models.DecimalField("消耗总额", max_digits=10, decimal_places=2, default=0)
    invoicenum = models.DecimalField("发票金额", max_digits=10, decimal_places=2, default=0,blank=True,null=True)
    cost = models.DecimalField("项目成本", max_digits=10, decimal_places=2, default=0)
    cost_explain = models.CharField("成本说明", max_length=100,blank=True)
    is_delete = models.BooleanField("是否被删除",default=False)

    def consume_minus_paid(self):
        return self.consume - self.settle
    topay_amount = property(consume_minus_paid)



    def paid_minus_cost(self):
        return self.settle-self.cost
    profit = property(paid_minus_cost)

    def save(self, force_insert=False, force_update=False, using=None,
        update_fields=None):
        if self.state != 'finish':
            self.cost = self.settle
            self.finish_time = None
        else:
            if not self.finish_time:
                self.finish_time = datetime.date.today()
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    class Meta:
        ordering = ["-time"]
    #---------------------------------------------------------
    #当前的
    #按天的
    #---------------------------------------------------------
    # ppreforconsume
    # ppreallconsume
    # allrefundnum
    # pprechannelconsume
    # pchannelrefundnum
    # pprewebconsume
    # pwebrefundnum
    # ppreforrec

class ProjectInvestData(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_data',on_delete=models.CASCADE)
    is_futou = models.BooleanField("是否复投", default=False)
    source = models.CharField("投资来源", choices=SOURCE, max_length=10)
    invest_mobile = models.CharField("投资手机号", max_length=11)
    invest_time = models.DateField("投资时间")
    invest_amount = models.DecimalField("投资金额", max_digits=10, decimal_places=2)
    invest_term = models.CharField("投资标期", max_length=13)
    settle_amount = models.DecimalField("结算金额", max_digits=10, decimal_places=2)
    return_amount = models.DecimalField("返现金额", max_digits=10, decimal_places=2, default=0)
    audit_time = models.DateTimeField("审核时间（二次导入时间）", null=True)
    state = models.CharField("审核状态", max_length=10, choices=AUDIT_STATE)
    remark = models.CharField("备注", max_length=100)


    def futou_des(self):
        return "复投" if self.is_futou else "首投"


class ProjectStatis(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_statis',on_delete=models.CASCADE)
    channel_consume = models.DecimalField("渠道消耗", max_digits=10, decimal_places=2, default=0)
    channel_return = models.DecimalField("渠道返现金额", max_digits=10, decimal_places=2, default=0)
    site_consume = models.DecimalField("网站消耗", max_digits=10, decimal_places=2, default=0)
    site_return = models.DecimalField("网站返现金额", max_digits=10, decimal_places=2, default=0)
    def consume(self):
        return self.channel_consume + self.site_consume
    def ret(self):
        return self.channel_return + self.site_return
    def __unicode__(self):
        return str(self.project_id) + self.project.name
    class Meta:
        ordering = ["-project__time"]

#点击查看项目详情：日期  项目名称  当前总待收  预估利润  昨日结算金额

class ProjectDetail(models.Model):
    date = models.DateField("日期", primary_key=True)
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_data',on_delete=models.CASCADE)
    total_to_rec = models.DecimalField("总待收", max_digits=10, decimal_places=2, null=True)
    budgeted_income = models.DecimalField("预估利润", max_digits=10, decimal_places=2, null=True)
    lastday_settle_num = models.DecimalField("昨日结算金额", max_digits=10, decimal_places=2, null=True)


class DayStatis(models.Model):
    date = models.DateField("日期", primary_key=True)
    start_num = models.IntegerField("正在进行的项目数")
    finish_num = models.IntegerField("已结项的项目数")
    invest_count = models.IntegerField("投资人数")
    ret_count = models.IntegerField("返现人数")
    invest_sum = models.DecimalField("投资金额", max_digits=10, decimal_places=2, null=True)
    consume_sum = models.DecimalField("消耗金额", max_digits=10, decimal_places=2, null=True)
    ret_invest_sum = models.DecimalField("返现投资金额", max_digits=10, decimal_places=2, null=True)
    ret_sum = models.DecimalField("返现费用", max_digits=10, decimal_places=2, null=True)
    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d")
    class Meta:
        ordering = ['-date']


class DBlock(models.Model):
    index = models.CharField("name",max_length=10,primary_key=True)
    description = models.CharField("description",max_length=30)


class OperatorLog(models.Model):
    """只记录删除，修改和导入数据的操作"""
    otime = models.DateTimeField("操作时间", default=timezone.now)
    oman = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="操作人",related_name="oman")
    oobj = models.CharField("操作资源uri",max_length=200)#如果是导入表格的话，记录导入表格的路径
    otype = models.CharField("操作类型",choices=OTYPE,max_length=2)


class fund_apply_log(models.Model):
    """费用申请"""
    """时间 项目名称 打款金额 打款时间 打款截图 对公对私  甲方公司名称 审核状态  备注 """
    date = models.DateField("日期", primary_key=True)
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_data',on_delete=models.CASCADE)
    fund_rec = models.CharField("打款金额")
    send_time = models.DateTimeField
    send_pic = models.CharField()
    fundtype= models.CharField("打款类型对公对私",choices=ACCOUNT_TYPE,max_length=2)
    audit_state = models.CharField("审核状态",choices=AUDIT_STATE)
    record = models.CharField()
    company = models.CharField("甲方公司名称")

class refund_apply_log(models.Model):
    """退款申请　日期  项目名称  甲方公司名称  平台名称  对公对私  是否已开票    预付款金额
       已消耗金额   退款金额   签约公司  甲方公司名称   开户行  银行帐号    退款原因  状态  """
    date = models.DateField("日期", primary_key=True)
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_data',on_delete=models.CASCADE)
    fund_rec = models.CharField("打款金额")
    send_time = models.DateTimeField
    send_pic = models.CharField()
    fundtype= models.CharField("打款类型对公对私",choices=ACCOUNT_TYPE,max_length=2)
    audit_state = models.CharField("审核状态",choices=AUDIT_STATE)
    record = models.CharField()
    company = models.CharField("甲方公司名称")

class invoice_apply_log(models.Model):
    """ 时间 项目名称 开票日期  发票类型  签约公司  甲方公司名称  开票金额  备注  状态 """
    date = models.DateField("日期", primary_key=True)
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_data',on_delete=models.CASCADE)
    fund_rec = models.CharField("打款金额")
    send_time = models.DateTimeField
    send_pic = models.CharField()
    fundtype= models.CharField("打款类型对公对私",choices=ACCOUNT_TYPE,max_length=2)
    audit_state = models.CharField("审核状态",choices=AUDIT_STATE)
    record = models.CharField()
    company = models.CharField("甲方公司名称")






# class ProDumpRecord(models):
#     project =models.ForeignKey(Project,on_delete=models.SET_NULL,verbose_name="项目")
#     rtype = models.CharField("首投/复投",choices=SUB_TYPE)
#     rinvestdate=models.DateField("投资日期",default=timezone.now)
#     rmobile = models.CharField("投资手机号",max_length=20)
#     rinvestnum = models.DecimalField("投资金额",max_digits=15)
#     rinverstperiod=models.IntegerField("投资标期")
#     rpreconsume = models.IntegerField("预估消耗")
#     rauditstate= models.CharField("审核状态")
#     rreduntnum=models.DecimalField("返现金额",blank=True,null=True)
#     rinverstorigin =models.CharField("投资来源")
#     record = models.CharField("备注")


