"""Library URL Configuration

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
from Book.views import homepage, get_books, delete_book, testing_log , update_book, soft_delete, active_books, inactive_books 
from newapp import views as n_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', homepage, name ='home'),
    path('show-books/', get_books, name ='show books'),
    path("delete-book/<int:id>/",delete_book , name="delete"),  
    path("update-book/<int:id>/",update_book , name="update"),  
    path("soft-delet-book/<int:id>/",soft_delete , name="soft_delete"),  
    path("active-books/",active_books , name="active_books"),  
    path("inactive-books/",inactive_books , name="inactive_books"),  
    path("test-logger/",testing_log , name="test_log"),  
    path("newapp/",n_views.newapp_greetings , name="newapp"),  
]
