from django.db import models
from account.models import User
from django.utils import timezone
import datetime
from decimal import Decimal
# Create your models here.

ACCOUNT_TYPE = {
    ('0','对公'),
    ('1','对私'),
}

IS_INVOICE = {
    ('0','是'),
    ('1','否'),
}

INVOICE_TYPE = {
    ('0','专票'),
    ('1','普票'),
}

SETTLE_STATE=(
    ('0', "预付款"),
    ('1', "后付款"),
    ('2', "日结"),
)
AUDIT_STATE = (
    ('0', '待审核'),
    ('1', '审核通过'),
    ('2', '审核未通过'),
)
PAUDIT_STATE = (
    ('0', '待审核'),
    ('1', '进行中'),
    ('2', '审核未通过'),
    ('4', '结项中'),#结项中等于待审核
    ('5', '已结项'),#已结项等于审核通过
    ('6', '结项失败'),#结项失败等于审核失败

)

SUB_TYPE = (
    ('1', '首投'),
    ('2', '复投'),
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
    #pid =models.CharField("项目编号", max_length=11, unique=True)
    contact=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="商务对接人",related_name="contact",blank=True,null=True)

    audituser=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="auditman",verbose_name="审核人",blank=True,null=True)
    name = models.CharField("项目名字", max_length=50)
    company= models.CharField("甲方公司名称", max_length=20)
    platname= models.CharField("平台名字", max_length=20)
    paccountype= models.CharField("账户类型",choices=ACCOUNT_TYPE,max_length=2)
    settleway= models.CharField("结算方式",choices=SETTLE_STATE, max_length=10)
    settle_detail= models.CharField("结算详情", max_length=30,blank=True,null=True)
    contract_company = models.CharField("签约公司", max_length=50)
    pcoperatedetail= models.CharField("合作详情", max_length=200)
    remark= models.CharField("备注", max_length=200,blank=True,null=True)
    state= models.CharField("审核状态",choices=PAUDIT_STATE, max_length=2,default='0')
    settle = models.DecimalField("结算费用", max_digits=10, decimal_places=2, default=0)
    psettlereason= models.CharField("结项原因", max_length=20,null=True)
    concluded_apply_date = models.DateField("结项申请日期", blank=True, null=True)
    concluded_audit_date = models.DateField("结项审核日期", blank=True, null=True)


    #auditstate= models.CharField("立项审核状态",choices=AUDIT_STATE, max_length=2)
    lanched_apply_date= models.DateField("立项申请日期",default=datetime.date.today)
    lanched_audit_date= models.DateField("立项审核日期",blank=True, null=True)
    lanched_refused_reason = models.CharField("立项拒绝原因",max_length=100,blank=True,null=True)
    conclued_refused_reason = models.CharField("结项拒绝原因",max_length=100,blank=True,null=True)
    consume = models.DecimalField("消耗总额", max_digits=10, decimal_places=2, default=0)
    invoicenum = models.DecimalField("发票金额", max_digits=10, decimal_places=2, default=0,blank=True,null=True)
    cost = models.DecimalField("项目成本", max_digits=10, decimal_places=2, default=0)
    cost_explain = models.CharField("成本说明", max_length=100,blank=True)
    is_delete = models.BooleanField("是否被删除",default=False)

    def consume_minus_paid(self):
        return self.consume - self.settle
    topay_amount = property(consume_minus_paid)



    def paid_minus_cost(self):
        if self.paccountype=="0":
            return self.settle-self.cost
        elif self.paccountype =="1":
            return self.settle*Decimal(0.94)-self.cost
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

    def __repr__(self):
            return "%s项目公司是%s项目名是%s,签约公司%s" % (self.id,self.company,self.name,self.contract_company)




    class Meta:
        ordering = ["-lanched_apply_date"]




    #---------------------------------------------------------
    #当前的
    #按天的
    #---------------------------------------------------------








class DBlock(models.Model):
    index = models.CharField("name",max_length=10,primary_key=True)
    description = models.CharField("description",max_length=30)


class OperatorLog(models.Model):
    """只记录删除，修改和导入数据的操作
        关于项目立项的操作，修改的操作
    普通用户只能看自己的记录
    管理员能看所有的记录

    """

    otime = models.DateTimeField("操作时间", default=timezone.now)
    oman = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="操作人",related_name="oman")
    oobj = models.CharField("操作资源uri",max_length=200)#如果是导入表格的话，记录导入表格的路径
    otype = models.CharField("操作类型",choices=OTYPE,max_length=2)


class FundApplyLog(models.Model):
    """费用申请"""
    """时间 项目名称 打款金额 打款时间 打款截图 对公对私  甲方公司名称 审核状态  备注 """
   # date = models.DateField("日期", primary_key=True)
    project = models.ForeignKey(Project, verbose_name="项目名", related_name='project_fund_apply',on_delete=models.CASCADE)
    apply_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="申请人",related_name="fundapplyuser",blank=True,null=True)
    audit_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="审核人",related_name="fundaudituser",blank=True,null=True)
    audituser = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="审核人", related_name="fundaudituser1",blank=True, null=True)
    fund_rec = models.DecimalField("打款金额", max_digits=10, decimal_places=2)
    send_pic = models.CharField("打款截图",max_length=200)
    fundtype= models.CharField("打款类型对公对私",choices=ACCOUNT_TYPE,max_length=2)
    state = models.CharField("审核状态",choices=AUDIT_STATE,max_length=2,blank=True,null=True)
    record = models.CharField("备注",max_length=200,blank=True,null=True)
    company = models.CharField("甲方公司名称",max_length=50)
    apply_date = models.DateField("申请日期", default=datetime.date.today)
    send_date = models.DateField("打款日期", default=datetime.date.today)
    audit_refused_reason = models.CharField("拒绝原因", max_length=100,blank=True,null=True)
    audit_date = models.DateField("审核日期", default=datetime.date.today)
    #is_delete = models.BooleanField("是否被删除",default=False)
    is_delete = models.BooleanField("是否被删除", default=False)

class RefundApplyLog(models.Model):
    """退款申请　日期  项目名称  甲方公司名称  平台名称  对公对私  是否已开票    预付款金额
       已消耗金额   退款金额   签约公司  甲方公司名称   开户行  银行帐号    退款原因  状态  """
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_refund_apply',on_delete=models.CASCADE)
    apply_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="申请人",related_name="refundapplyuser",blank=True,null=True)
    audit_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="审核人",related_name="refundaudituser",blank=True,null=True)
    audituser = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="审核人1", related_name="refundaudituser1",blank=True, null=True)
    inprest = models.DecimalField("预付款金额", max_digits=10, decimal_places=2)
    refund_rec = models.DecimalField("退款金额", max_digits=10, decimal_places=2)
    platname= models.CharField("平台名字", max_length=20)
    consume_sum = models.DecimalField("已消耗金额", max_digits=10, decimal_places=2)
    refund_reason = models.CharField("退款原因",max_length=200)
    fundtype= models.CharField("打款类型对公对私",choices=ACCOUNT_TYPE,max_length=2)
    is_invoice= models.CharField("是否已开票",choices=IS_INVOICE,max_length=2)
    record = models.CharField("备注",max_length=200,blank=True,null=True)
    company = models.CharField("甲方公司名称",max_length=50)
    contract_company = models.CharField("签约公司", max_length=50)
    bank_account = models.CharField("银行账号", max_length=50)
    bank = models.CharField('开户银行', max_length=50)
    #state = models.CharField("项目状态", choices=PAUDIT_STATE, max_length=20)
    apply_date = models.DateField("申请日期", default=datetime.date.today)
    audit_refused_reason = models.CharField("拒绝原因", max_length=100,blank=True)
    audit_date = models.DateField("审核日期", default=datetime.date.today)
    is_delete = models.BooleanField("是否被删除",default=False)
    state = models.CharField("审核状态",choices=AUDIT_STATE,max_length=2,blank=True,default='0')


class InvoiceApplyLog(models.Model):
    """ 时间 项目名称 开票日期  发票类型  签约公司  甲方公司名称  开票金额  备注  状态 """
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_invoice_apply',on_delete=models.CASCADE)
    apply_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="申请人",related_name="invoiceapplyuser",blank=True,null=True)
    audit_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="审核人",related_name="invoiceaudituser",blank=True,null=True)
    audituser = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="审核人", related_name="invoiceaudituser1",blank=True, null=True)
    invoice_num = models.DecimalField("开票金额", max_digits=10, decimal_places=2)
    invoice_date = models.DateField("开票日期", default=datetime.date.today)
    invoice_type= models.CharField("发票类型",choices=INVOICE_TYPE,max_length=2)
    #invoice_state = models.CharField("审核状态",choices=AUDIT_STATE,max_length=2,blank=True)
    audit_state = models.CharField("审核状态",choices=AUDIT_STATE,max_length=2,blank=True)
    record = models.CharField("备注", max_length=200,null=True,blank=True)
    company = models.CharField("甲方公司名称",max_length=50)
    putaxmanid= models.CharField("纳税人识别号",max_length=50)
    contract_company = models.CharField("签约公司", max_length=50)
    bank = models.CharField('开户银行', max_length=50)
    bank_account = models.CharField("银行账号", max_length=50)
    regaddress = models.CharField('注册地址', max_length=50)
    mobile = models.CharField('电话', max_length=13)
    apply_date = models.DateField("申请日期", default=datetime.date.today)
    audit_refused_reason = models.CharField("拒绝原因", max_length=100,blank=True)
    audit_date = models.DateField("审核日期", default=datetime.date.today)
    is_delete = models.BooleanField("是否被删除",default=False)
    state = models.CharField("审核状态",choices=AUDIT_STATE,max_length=2,default='0')
    return_num = models.DecimalField("返现金额", max_digits=10, decimal_places=2,blank=True,null=True)

# class ProjectRecord(models.Model):
#     """ 项目详情 """
#     project = models.ForeignKey(Project, verbose_name="项目", related_name='project_invoice_apply',on_delete=models.CASCADE)
#     apply_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="申请人",related_name="invoiceapplyuser",blank=True,null=True)
#     audit_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="审核人",related_name="invoiceaudituser",blank=True,null=True)
#     invoice_num = models.DecimalField("开票金额", max_digits=10, decimal_places=2)
#     invoice_date = models.DateField("开票日期", default=datetime.date.today)

class ProjectInvestDataModel(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_investdata',on_delete=models.CASCADE)
    is_futou = models.BooleanField("是否复投", default=False)
    apply_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="导入人",related_name="importinvestapplyuser",blank=True,null=True)
    audit_man=models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="审核人",related_name="importinvestaudituser",blank=True,null=True)

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

    def __repr__(self):
        return "%s投资记录,手机是%s,项目名是%s" % (self.id, self.invest_mobile, self.project.name)

    def futou_des(self):
        return "复投" if self.is_futou else "首投"

class ProjectInvestData(models.Model):
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_investdata2',on_delete=models.CASCADE)
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


