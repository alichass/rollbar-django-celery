from django.http import HttpResponse
import logging

logger = logging.getLogger('rbexample')

def home(request):
    logger.warning('hello from home')
    return HttpResponse('Welcome to the homepage!')

def broken(request):
    data = None
    return data['bork']


from tasks import add, sub

def delay_broken(request):
    res = add.delay(4, 4)
    return HttpResponse(res.get(timeout=5))

def delay_ok(request):
    res = sub.delay(8, 4)
    return HttpResponse(res.get(timeout=1))
