from django.db import models
from django.db import models

# Create your models here.

class table1(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'table1'

class table2(models.Model):
    name1 = models.CharField(max_length=100)
    age1 = models.IntegerField()
    time1 = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'table2'

