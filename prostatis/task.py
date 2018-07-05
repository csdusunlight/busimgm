from __future__ import absolute_import
from celery import app
from celery import group

@app.task
def add(x, y):
    return x + y