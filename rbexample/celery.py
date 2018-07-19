from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rbexample.settings')

app = Celery('rbtasks', backend='rpc://', broker='redis://localhost:6379/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

from celery.signals import task_failure

import rollbar

@task_failure.connect
def handle_task_failure(**kw):
    rollbar.report_exc_info(extra_data=kw)
