#coding:utf-8
import datetime

from django.core.management import BaseCommand
from django.db.models import Sum, Count, Q
from prostatis.models import ProjectDayStatis, UserDayStatis, DayStatis, UserStatis
from project.models import ProjectInvestDataModel, Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        statis_for_projectday()
        statis_for_userday()
        statis_for_day()
        statis_for_project()
        statis_for_user()

def statis_for_projectday():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = ProjectInvestDataModel.objects.filter(invest_time__gte=seven_days_ago).\
        values('project_id', 'invest_time').annotate(
        invest_amount=Sum('invest_amount'),
        consume_amount=Sum('settle_amount'),
        return_amount=Sum('return_amount'))
    for item in queryset:
        defaults = dict(consume_amount=item['consume_amount'],invest_amount=item['invest_amount'],
                  return_amount=item['return_amount'],)
        ProjectDayStatis.objects.update_or_create(project_id=item['project_id'], date=item['invest_time'],
                    defaults=defaults)

def statis_for_userday():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = ProjectDayStatis.objects.filter(date__gte=seven_days_ago). \
        values('project__contact_id', 'date').annotate(
        invest_count=Count('id'),
        invest_amount=Sum('invest_amount'),
        consume_amount=Sum('consume_amount'),
        return_amount=Sum('return_amount'))
    for item in queryset:
        defaults = dict(consume_amount=item['consume_amount'], invest_amount=item['invest_amount'],
                        return_amount=item['return_amount'], invest_count=item['invest_count'])
        UserDayStatis.objects.update_or_create(user_id=item['project__contact_id'], date=item['date'], defaults=defaults)

def statis_for_day():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = ProjectInvestDataModel.objects.filter(invest_time__gte=seven_days_ago).values('invest_time') \
        .annotate(invest_count=Count('id'),
                  return_count=Count('id', filter=Q(state='1')),
                  return_invest_amount=Sum('invest_amount', filter=Q(state='1')),
                  invest_amount=Sum('invest_amount'),
                  consume_amount=Sum('settle_amount'),
                  return_amount=Sum('return_amount')
        )
    for item in queryset:
        date = item.pop('invest_time')
        item['start_num'] = Project.objects.filter(lanched_apply_date=today).count()
        item['finish_num'] = Project.objects.filter(lanched_apply_date=today).count()
        DayStatis.objects.update_or_create(date=date,defaults=item)

def statis_for_project():
    queryset = ProjectInvestDataModel.objects.filter(state='1').values('project_id') \
        .annotate(consume=Sum('settle_amount'),cost=Sum('return_amount'))
    for item in queryset:
        id = item.pop('project_id')
        Project.objects.filter(id=id).update(**item)

def statis_for_user():
    queryset = UserDayStatis.objects.values('user_id').annotate(invest_count=Sum('invest_count'),
        return_amount=Sum('return_amount'),invest_amount=Sum('invest_amount'),consume_amount=Sum('consume_amount'),)
    for item in queryset:
        user_id = item.pop('user_id')
        item['start_num'] = Project.objects.filter(contact_id=user_id, state__in=['00', '01', '06']).count()
        item['finish_num'] = Project.objects.filter(contact_id=user_id, state__in=['04', '05']).count()
        UserStatis.objects.update_or_create(user_id=user_id, defaults=item)
        # defaults = dict(invest_count=item['invest_count'], return_count=item['return_count'],
        #                 invest_amount=item['invest_amount'], return_invest_amount=item['return_invest_amount'],
        #                 consume_amount=item['consume_amount'], return_amount=item['invest_amount'],)
        #
        # ProjectDayStatis.objects.update_or_create(project_id=item['project_id'], date=item['invest_time'],
        #                                           defaults=defaults)

        # todaynum = yesterdaynum + todaystatic['invest_sum'] - todaystatic['settle_sum']
        # current_pro = ProjectDayStatis.project.paccountype
        # # 如果是公账，就0.94*
        # preprofit = todaystatic['settle_sum'] * 0.94 - todaystatic['return_amount'] if current_pro == "0" else \
        #     todaystatic['settle_sum'] - todaystatic['return_amount']
        # update_fields['total_to_rec'] = todaynum
        # update_fields['budgeted_income'] = preprofit
        # update_fields['lastday_settle_num'] = todaystatic['settle_sum']
        # ProjectDayStatis.objects.update_or_create(date=today, defaults=update_fields)