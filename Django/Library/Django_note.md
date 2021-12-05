# Django


```python
Even though 'D' is silent ,
Django is quite voilent framework.

Mohammad Sharique
```
## Creating project

1. open cmd and type
```cmd
django-admin startproject project__name
```
It will create following files in directory

```python
project_name/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
2. running server
   
```python
python manage.py runserver
```
If everthing is fine then it will execute properly.

3. To change default port if needed
```python
python manage.py runserver 8000
```
where 8000 is port number you want to switch

## Creating a app

1. type 
```python
python manage.py startapp app_name
```
it will create following folder structure
```python
app_name/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
2. Register your app in admin.py
``` python
from .models import app_name

admin.site.register(app_name)
```
## Changing DATABASE from sql3lite to mysql

1. Add following code in your project_name settings
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'b5_library',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
## Creating models in models.py
1. creat models what you needed.
2. Creating migration using
``` python
python manage.py makemigrations
```
3. Migrating the modules into the database
```ptyhon
python manage.py migrate
```
## Creating Superuser 
1. Type following command
```python
python manage.py createsuperuser
```