#coding:utf-8
import datetime

from django.core.management import BaseCommand
from django.db.models import Sum, Count, Q

from account.models import User
from prostatis.models import ProjectDayStatis, UserDayStatis, DayStatis, UserStatis
from project.models import ProjectInvestDataModel, Project


# class Command(BaseCommand):
    # def handle(self, *args, **options):
    #     users = User.objects.all()
    #     today = datetime.date.today()
    #     projects = Project.objects.all(state)
    #     for user in users:
    #         ProjectDayStatis.objects.create(project_id=project_id, date=date,
    #                 defaults=item)
    #     UserDayStatis.objects.update_or_create(user_id=user_id, date=date, defaults=item)
    #     DayStatis.objects.update_or_create(date=date,defaults=item)
    #     UserStatis.objects.update_or_create(user_id=user_id, defaults=item)
