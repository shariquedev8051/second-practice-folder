
from django.db import models
from django.db.models.manager import Manager



#* id, name, qty, price, is_published, auther
# Custom model manager 

class ActiveBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = 'N')


class InactiveBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = 'Y')



class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null =True)
    is_deleted =models.CharField(max_length=1, default='N')
    active_books = ActiveBookManager()
    inactive_books = InactiveBookManager()
    objects = Manager() # defualt manager if you need Book.objects.all()

    def __str__(self):
        return f'{self.__dict__}'


    class Meta:
        db_table = 'book'

    

    


