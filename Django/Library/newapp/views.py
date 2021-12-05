
from django.http import HttpResponse
import logging
logger1 = logging.getLogger('newapp_logger')
import time
def newapp_greetings(request):
    logger1.error("Page has been accessed!!")
    return HttpResponse("<h1>Hello There!!<h1>")
