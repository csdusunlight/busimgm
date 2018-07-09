from __future__ import absolute_import
from celery import app
from celery import group
import datetime
import time
from prostatis.models import ProjectStatis,DayStatis,ProjectDayDetail
from project.models import ProjectInvestData
from project.models import Project
from django.db.models import Count, Case, When, CharField, Sum, IntegerField, Q


@app.task
def add(x, y):
    begin_time = time.time()
    today = datetime.date.today()
    from django.db import connection, transaction
    #         return row
    update_fields = {}
    update_fields['start_num'] = Project.objects.filter(state='start').count()
    update_fields['finish_num'] = Project.objects.filter(state='finish').count()
    update_fields['invest_count'] = ProjectInvestData.objects.filter(invest_time=today).count()
    statdic = ProjectInvestData.objects.filter(invest_time=today).aggregate(invest_sum=Sum('invest_amount'),
                                                                            consume_sum=Sum('settle_amount'))
    update_fields['ret_count'] = ProjectInvestData.objects.filter(invest_time=today, state='0').count()
    statdic_pass = ProjectInvestData.objects.filter(invest_time=today, state='0').aggregate(
        ret_invest_sum=Sum('invest_amount'), ret_sum=Sum('return_amount'))
    update_fields.update(statdic)
    update_fields.update(statdic_pass)
    obj, created = DayStatis.objects.update_or_create(date=today, defaults=update_fields)

    """增加对项目每日数据详情的结算
       日期,项目,总待收,预估利润,昨日结算金额  
       原数据是investdata来的
       对investdata进行统计，结果得到
    """
    """如果是公账,那么settle*0.94-cost
        如果是私账,那么settle-cost
    """
    cursor = connection.cursor()
    cursor.execute("select a.project_id, a.source,sum(a.settle_amount) as sumofsettle, \
                                sum(a.return_amount) as sumofret \
                                b.paccounttype as accounttype\
                                from project_admin_projectinvestdata a \
                                left join project_project as b \
                                on a.project_id = b.id \
                                where audit_time =today and state='1'\
                                group by a.project_id, a.source")
    row = cursor.fetchall()

    """已经拿出来所有的投资记录,然后根据项目名称，计算当前总待收　consume -settle　
                        budgeted_income        预估利润  结算费用减去消耗　　settle -  cost
                                
    
    """
    project_dic = {}
    for item in row:
        id = item[0]
        source = item[1]
        consume = item[2]
        ret = item[3]
        accounttype = item[4]
        attr = {}
        if project_dic.get(id,False):
            attr = project_dic[id]
        else:
            project_dic[id] = attr
        if source == 'site':
            attr['site_consume'] = consume
            attr['site_return'] = ret
        elif source == 'channel':
            attr['channel_consume'] = consume
            attr['channel_return'] = ret
    #         print project_dic
    for id, kwarg in project_dic.items():
        obj, created = ProjectStatis.objects.update_or_create(project_id=id, defaults=kwarg)
        aimpro=Project.objects.filter(id=id).update(consume=obj.consume())

        ProjectDayDetail.objects.create(project=aimpro,
                                        date=datetime.datetime.today,
                                        total_to_rec=,
                                        budgeted_income=,
                                        lastday_settle_num=,)

    update_fields = {}
    update_fields['date'] = datetime.date.today()
    update_fields['total_to_rec'] = Project.objects.filter(state='start').count()
    #aimpro =
    update_fields['budgeted_income'] = Project.objects.filter(state='start').count()
    update_fields['lastday_settle_num'] = Project.objects.filter(state='start').count()




    return '0'