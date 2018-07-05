# coding:utf-8
'''
Created on 2018年5月21日

@author: lch
'''
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runitem.settings')

app = Celery('busimgm')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
        'add-every-4-seconds': {
            'task': 'Activity.tasks.mul',
            'schedule': 4.0,
            'args': (16, 16)
        },
        'add-every-day-1:00': {
            'task': 'tasks.add',
            'schedule': crontab(hour=1, minute=0),
            'args': (16, 16),
        },
}
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, add.s(10,20), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(10.0, add.s(10,100), expires=10)

# Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         test.s('Happy Mondays!'),
#     )

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()