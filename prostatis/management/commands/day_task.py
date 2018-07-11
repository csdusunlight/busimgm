#coding:utf-8
import datetime

from django.core.management import BaseCommand

from account.models import User
from prostatis.models import ProjectDayStatis, UserDayStatis, DayStatis, UserStatis
from project.models import Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        today = datetime.date.today()
        projects = Project.objects.filter(state__in=['01','04','06'])
        for project in projects:
            ProjectDayStatis.objects.update_or_create(project=project, date=today)
        for user in users:
            UserDayStatis.objects.update_or_create(user=user, date=today)
            UserStatis.objects.update_or_create(user=user)
        DayStatis.objects.update_or_create(date=today)

