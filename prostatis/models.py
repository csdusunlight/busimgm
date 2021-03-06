from django.db import models
from account.models import User
from project.models import Project
from project.models import AUDIT_STATE
from django.utils import timezone
import datetime
SOURCE=(
    ('site', "网站"),
    ('channel', "渠道"),
)
#分析数据
#class Prostatis(models):
    # ppreforconsume
    # ppreallconsume
    # allrefundnum
    # pprechannelconsume
    # pchannelrefundnum
    # pprewebconsume
    # pwebrefundnum
    # ppreforrec




class ProjectDayStatis(models.Model):
    '''项目每日数据详情'''
    date = models.DateField("日期")
    project = models.ForeignKey(Project, verbose_name="项目", related_name='project_day_statis',on_delete=models.CASCADE)
    invest_amount = models.DecimalField(u"投资金额", max_digits=10, decimal_places=2, default=0)
    invest_count = models.IntegerField(u"投资人数", default=0)
    consume_amount = models.DecimalField(u"消耗费用", max_digits=10, decimal_places=2, default=0)
    return_amount = models.DecimalField(u"返现费用", max_digits=10, decimal_places=2, default=0)
    return_count = models.IntegerField("返现人数", default=0)
    return_invest_amount = models.DecimalField("返现投资金额", max_digits=10, decimal_places=2, null=True, default=0)
    def budgeted_income(self):
        return self.consume_amount - self.return_amount
    class Meta:
        unique_together = (('date', 'project'),)

class UserDayStatis(models.Model):
    date = models.DateField("日期")
    user = models.ForeignKey(User, verbose_name="用户", related_name='user_day_statis', on_delete=models.CASCADE)
    # total_to_rec = models.DecimalField("总待收", max_digits=10, decimal_places=2, null=True)
    # budgeted_income = models.DecimalField("预估利润", max_digits=10, decimal_places=2, null=True)
    start_num = models.IntegerField("申请项目数", default=0)
    finish_num = models.IntegerField("结项项目数", default=0)
    invest_amount = models.DecimalField(u"投资金额", max_digits=10, decimal_places=2, default=0)
    consume_amount = models.DecimalField(u"消耗费用", max_digits=10, decimal_places=2, default=0)
    return_amount = models.DecimalField(u"返现费用", max_digits=10, decimal_places=2, default=0)
    invest_count = models.IntegerField("投资人数", default=0)
    return_count = models.IntegerField("返现人数", default=0)
    return_invest_amount = models.DecimalField("返现投资金额", max_digits=10, decimal_places=2, null=True, default=0)
    def budgeted_income(self):
        return self.consume_amount - self.return_amount
    class Meta:
        unique_together = (('date', 'user'),)


class DayStatis(models.Model):
    date = models.DateField("日期", primary_key=True)
    start_num = models.IntegerField("申请项目数", default=0)
    finish_num = models.IntegerField("结项项目数", default=0)
    invest_count = models.IntegerField("投资人数", default=0)
    return_count = models.IntegerField("返现人数", default=0)
    invest_amount = models.DecimalField("投资金额", max_digits=10, decimal_places=2, null=True, default=0)
    consume_amount = models.DecimalField("消耗金额", max_digits=10, decimal_places=2, null=True, default=0)
    return_invest_amount = models.DecimalField("返现投资金额", max_digits=10, decimal_places=2, null=True, default=0)
    return_amount = models.DecimalField("返现费用", max_digits=10, decimal_places=2, null=True, default=0)
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    class Meta:
        ordering = ['-date']



class UserStatis(models.Model):
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
    online_num = models.IntegerField("正在进行的项目数", default=0)
    to_consume_amount = models.DecimalField("待消耗金额", max_digits=10, decimal_places=2, null=True, default=0)
    to_consume_num = models.IntegerField("待消耗项目数", default=0)
    to_settle_amount = models.DecimalField("待结算金额", max_digits=10, decimal_places=2, null=True, default=0)
    to_settle_num = models.IntegerField("待结算项目数", default=0)
    # start_num = models.IntegerField("正在进行的项目数", default=0)
    # finish_num = models.IntegerField("已结项的项目数", default=0)
    # invest_count = models.IntegerField("投资人数", default=0)
    # invest_amount = models.DecimalField("投资金额", max_digits=10, decimal_places=2, null=True, default=0)
    # consume_amount = models.DecimalField("消耗金额", max_digits=10, decimal_places=2, null=True, default=0)
    # return_amount = models.DecimalField("返现费用", max_digits=10, decimal_places=2, null=True, default=0)
    def __str__(self):
        return self.user.uid
