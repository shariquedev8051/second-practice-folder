from django.shortcuts import render
from .forms import GeekForm

# Create your views here.
def home_view(request):
    context = {}
    context['form'] = GeekForm()
    return render (request, "home.html", context)