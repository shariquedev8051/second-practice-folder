from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Profile(models.Model):
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    is_verified = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username