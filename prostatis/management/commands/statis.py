#coding:utf-8
import datetime

from django.core.management import BaseCommand
from django.db.models import Sum, Count, Q, F
from prostatis.models import ProjectDayStatis, UserDayStatis, DayStatis, UserStatis
from project.models import ProjectInvestDataModel, Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        # statis_for_projectday()
        # statis_for_userday()
        # statis_for_day()
        # statis_for_project()
        statis_for_user()

def statis_for_projectday():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = ProjectInvestDataModel.objects.filter(invest_time__gte=seven_days_ago).\
        values('project_id', 'invest_time').annotate(
        invest_count=Count('id'),
        return_count=Count('id', filter=Q(state='1')),
        return_invest_amount=Sum('invest_amount', filter=Q(state='1')),
        invest_amount=Sum('invest_amount'),
        consume_amount=Sum('settle_amount'),
        return_amount=Sum('return_amount'))
    for item in queryset:
        project_id = item.pop('project_id')
        date = item.pop('invest_time')
        ProjectDayStatis.objects.update_or_create(project_id=project_id, date=date,
                    defaults=item)

def statis_for_userday():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = ProjectDayStatis.objects.filter(date__gte=seven_days_ago). \
        values('project__contact_id', 'date').annotate(
        invest_count=Count('id'),
        invest_amount=Sum('invest_amount'),
        consume_amount=Sum('consume_amount'),
        return_amount=Sum('return_amount'),
        return_count = Sum('return_count'),
        return_invest_amount = Sum('return_invest_amount')
    )

    for item in queryset:
        user_id = item.pop('project__contact_id')
        date = item.pop('date')
        UserDayStatis.objects.update_or_create(user_id=user_id, date=date, defaults=item)

    queryset1 = Project.objects.filter(state__in=['1','4','6'], lanched_audit_date=today).values('contact_id').annotate(start_num=Count('*'))
    queryset2 = Project.objects.filter(state='5', concluded_audit_date=today).values('contact_id').annotate(finish_num=Count('*'))
    for item in list(queryset1) + list(queryset2):
        user_id = item.pop('contact_id')
        UserDayStatis.objects.update_or_create(user_id=user_id, date=today, defaults=item)

def statis_for_day():
    today = datetime.datetime.today()
    seven_days_ago = today - datetime.timedelta(days=7)
    queryset = UserDayStatis.objects.filter(date__gte=seven_days_ago).values('date') \
        .annotate(
                  invest_count=Count('id'),
                  invest_amount=Sum('invest_amount'),
                  consume_amount=Sum('consume_amount'),
                  return_amount=Sum('return_amount'),
                  return_count=Sum('return_count'),
                  return_invest_amount=Sum('return_invest_amount'),
                  start_num = Sum('start_num'),
                  finish_num = Sum('finish_num'),
        )
    for item in queryset:
        date = item.pop('date')
        DayStatis.objects.update_or_create(date=date,defaults=item)

def statis_for_project():
    queryset = ProjectInvestDataModel.objects.filter(state='1').values('project_id') \
        .annotate(consume=Sum('settle_amount'),cost=Sum('return_amount'))
    for item in queryset:
        id = item.pop('project_id')
        Project.objects.filter(id=id).update(**item)

def statis_for_user():
    # queryset = UserDayStatis.objects.values('user_id').annotate(
    #         invest_count=Sum('invest_count'),
    #         return_amount=Sum('return_amount'),
    #         invest_amount=Sum('invest_amount'),
    #         consume_amount=Sum('consume_amount'),
    #         start_num=Sum('start_num'),
    #         finish_num=Sum('finish_num'),
    # )
    # for item in queryset:
    #     user_id = item.pop('user_id')
    #     online_num = Project.objects.filter(state__in=['1','4','6']).count()
    #     UserStatis.objects.update_or_create(user_id=user_id, defaults=item)
    queryset = Project.objects.all().values('contact_id').annotate(
        online_num = Count('id', filter=Q(state__in=['1','4','6'])),
        to_consume_amount = Sum(F('settle')-F('cost'), filter=Q(settle__gt=F('cost'))),
        to_consume_num = Count('id', filter=Q(settle__gt=F('cost'))),
        to_settle_amount = Sum(F('cost')-F('settle'), filter=Q(settle__lt=F('cost'))),
        to_settle_num = Count('id', filter=Q(settle__lt=F('cost'))),
    )
    for item in queryset:
        user_id = item.pop('contact_id')
        UserStatis.objects.update_or_create(user_id=user_id, defaults=item)
    # to_settle_num = Project.objects.aggregate(settle__lt=F('cost')).count()
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