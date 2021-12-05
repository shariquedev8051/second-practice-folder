from django.shortcuts import render
from django.http import HttpResponse
from django.template.base import Template
from django.template.response import TemplateResponse

# Create your views here.

def home(request):
    print('In view function')
    return HttpResponse("<h1>Hello you are in home view response</h1>")

def greet(request):
    print('In view function')
    return HttpResponse("<h1>Hello you are in greet view response</h1>")

def function(request):
    print('In view function')
    return HttpResponse("<h1>Hello you are in function view response</h1>")

def exc_view(request):
        print("In exc_view")
        print(15/0)
        return HttpResponse("Hello exc_view response....!")

def template_view(request):
    print("In template view")
    context = {'name':'sharique'}
    return TemplateResponse(request, template="base.html", context=context)