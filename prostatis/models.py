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
    total_to_rec = models.DecimalField("总待收", max_digits=10, decimal_places=2, null=True)
    budgeted_income = models.DecimalField("预估利润", max_digits=10, decimal_places=2, null=True)
    lastday_settle_num = models.DecimalField("昨日结算金额", max_digits=10, decimal_places=2, null=True)
    class Meta:
        unique_together = (('date', 'project'),)
    #lastday_settled_pro_num = models.IntegerField("昨日结算项目数",null=True)

class UserDayStatis(models.Model):
    date = models.DateField("日期")
    user = models.ForeignKey(User, verbose_name="用户", related_name='user_day_statis', on_delete=models.CASCADE)
    total_to_rec = models.DecimalField("总待收", max_digits=10, decimal_places=2, null=True)
    budgeted_income = models.DecimalField("预估利润", max_digits=10, decimal_places=2, null=True)
    lastday_settle_num = models.DecimalField("昨日结算金额", max_digits=10, decimal_places=2, null=True)
    class Meta:
        unique_together = (('date', 'user'),)


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
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    class Meta:
        ordering = ['-date']


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
    def __str__(self):
        return str(self.project_id) + self.project.name
    class Meta:
        ordering = ["-project__time"]

class UserStatis(models.Model):
    user = models.OneToOneField(User, verbose_name="用户", on_delete=models.CASCADE)
    start_num = models.IntegerField("正在进行的项目数")
    finish_num = models.IntegerField("已结项的项目数")
    invest_count = models.IntegerField("投资人数")
    ret_count = models.IntegerField("返现人数")
    invest_sum = models.DecimalField("投资金额", max_digits=10, decimal_places=2, null=True)
    consume_sum = models.DecimalField("消耗金额", max_digits=10, decimal_places=2, null=True)
    ret_invest_sum = models.DecimalField("返现投资金额", max_digits=10, decimal_places=2, null=True)
    ret_sum = models.DecimalField("返现费用", max_digits=10, decimal_places=2, null=True)
    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
