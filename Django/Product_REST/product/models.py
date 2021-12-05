from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    balance = models.IntegerField()
    email = models.EmailField()

class Address(models.Model):
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    pincode = models.IntegerField()
    pincode = models.IntegerField()
    cat = models.CharField(max_length=100)
    customer = models.ManyToManyField(Customer, on_delete=models.CASCADE)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, on_delete=models.CASCADE)