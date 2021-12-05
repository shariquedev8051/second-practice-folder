# Book project

1. create models in book in model.py
```python
class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null =True)


    def __str__(self):
        return f'{self.__dict__}'


    class Meta:
        db_table = 'book'
```
2. register it in book in admin.py
```python 
from .models import Book

admin.site.register(BOOk)
```
3. Make migrations
4. Create database befor migrate
5. Check/ Migrate
6. Create superuser
7. Fill credintials of your desire
8. Home address us 127.0.0.1.8000
9. Go into views :   
There is a defualt argument known as 'request' for e.g  

    ```python
    def func(request):
        print('In func')
        print(request.methode) # to know requst type
    ```
10. Go into url 
```python
from Book.views import func
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',func),
]

```
11. in views
```python
from django.http import HttpResponse
def func(request):
    print(request.method) #? to see the type of request
    print('----------------In func-------------') #? testing purpose
    return HttpResponse('Hi welcome to web page')
    # return JsonResponse({'key':'value'})
```

12. Create template in project folder
13. Rendering data showing html file on browser tab 
14. Creating Home page in views
```python
def homepage(request):# we have to return something
    return HttpResponse('Hi welcome to homepage')
    return render(request , template_name = 'base.html')
```
15.    http status code
    200 -- success
    404 -- page note found

16. Creating form