from django.db import connection, transaction
from project.models import  ProjectInvestDataModel,Project
from prostatis.models import ProjectStatis,DayStatis,ProjectDayStatis,UserDayStatis
import datetime
from django.db.models import Sum,F

today = datetime.datetime.today()
cursor = connection.cursor()
cursor.execute("select a.project_id, a.source, sum(a.settle_amount) as sumofsettle, \
                            sum(a.return_amount) as sumofret from project_ProjectInvestDataModel a \
                            group by a.project_id, a.source")
row = cursor.fetchall()
project_dic = {}
for item in row:
    id = item[0]
    source = item[1]
    consume = item[2]
    ret = item[3]
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
    Project.objects.filter(id=id).update(consume=obj.consume())
#         return row
update_fields = {}
update_fields['start_num'] = Project.objects.filter(state='start').count()
update_fields['finish_num'] = Project.objects.filter(state='finish').count()
update_fields['invest_count'] = ProjectInvestDataModel.objects.filter(invest_time=today).count()
statdic = ProjectInvestDataModel.objects.filter(invest_time=datetime.datetime.today()).aggregate(invest_sum=Sum('invest_amount'),
                                                                        consume_sum=Sum('settle_amount'))
update_fields['ret_count'] = ProjectInvestDataModel.objects.filter(invest_time=today, state='0').count()
statdic_pass = ProjectInvestDataModel.objects.filter(invest_time=datetime.datetime.today(), state='0').aggregate(
    ret_invest_sum=Sum('invest_amount'), ret_sum=Sum('return_amount'))
update_fields.update(statdic)
update_fields.update(statdic_pass)
obj, created = DayStatis.objects.update_or_create(date=today, defaults=update_fields)


#更新所有的每日项目的每个人的明细
#项目详情:到项目详情　　单个项目的每天信息　日期   当前总待收   预估利润    今日结算金额
update_fields={}
today=datetime.datetime.today()
yesterdaynum   =ProjectDayStatis.objects.filter(date=yesteday)[1]
todaystatic=ProjectInvestDataModel.objects.filter(invest_time=today).aggregate(invest_amount=sum('invest_amout'),
                                                                    settle_amount=sum('settle_amount'),
                                                                    return_amount=sum('return_amount'))
todaynum = yesterdaynum + todaystatic['invest_sum']-todaystatic['settle_sum']
current_pro = ProjectDayStatis.project.paccountype
#如果是公账，就0.94*
preprofit =todaystatic['settle_sum']*0.94-todaystatic['return_amount'] if current_pro=="0"  else todaystatic['settle_sum']-todaystatic['return_amount']
update_fields['total_to_rec']=todaynum
update_fields['budgeted_income']=preprofit
update_fields['lastday_settle_num']=todaystatic['settle_sum']
ProjectDayStatis.objects.update_or_create(date=today, defaults=update_fields)

#当前总待收＝过去总待收　减去过去一天内结算的费用　加上增加的没结算分

#aimUserDayStatis
update_fields={}
today = datetime.datetime.today()
UserDayStatis = ProjectDayStatis.objects.filter(date=today).values("project__contact_id").\
    aggregate(invest_amount=sum('invest_amount'), settle_amount=sum('settle_amount'),
        return_amount=sum('return_amount'))
update_fields.update(UserDayStatis)

todaynum = yesterdaynum + todaystatic['invest_sum']-UserDayStatis['settle_sum']
current_pro = ProjectDayStatis.project.paccountype
preprofit =todaystatic['settle_sum']*0.94-todaystatic['return_amount'] if current_pro=="0"  else todaystatic['settle_sum']-todaystatic['return_amount']
update_fields['total_to_rec']=todaynum
update_fields['budgeted_income']=preprofit
update_fields['lastday_settle_num']=todaystatic['settle_sum']
UserDayStatis.objects.update_or_create(date=today,defaults=update_fields)



