from django.contrib import admin
from.models import Extended_user
# Register your models here.

@admin.register(Extended_user)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
