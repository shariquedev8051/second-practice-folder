from django.contrib import admin
from .models import Employee, Licence, Project, Task
# Register your models here.

admin.site.register([Employee, Licence, Project, Task])