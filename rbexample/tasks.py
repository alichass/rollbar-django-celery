from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    z = x + y
    foo = bar
    return z

@shared_task
def sub(x, y):
    logger.info('Hello from sub')
    z = x - y
    return z
