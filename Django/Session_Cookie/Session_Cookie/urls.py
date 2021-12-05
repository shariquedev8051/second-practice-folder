"""Session_Cookie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('scookie/', views.setcookie, name="sc"),
    path('home/', views.homepage, name="home"),
    path('gcookie/', views.getcookie, name="show-cookie"),
    path('dcookie/', views.delete_cookies, name="dc"),
    path('testcookie/', views.cookie_session),
    path('deletecookie/', views.cookie_delete),
    path('demo_view/', views.demo_view),
    path('create_session/', views.create_session),
    path('show_session/', views.show_session_data),
    path('delete_session/', views.session_delet),
]
 