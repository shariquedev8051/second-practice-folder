from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import logging
import time
logger = logging.getLogger('test_logger')

def homepage(request):

    for i in range(10):
        logger.info("Hi count {i}")
        time.sleep(1)
    return HttpResponse("Hello there")