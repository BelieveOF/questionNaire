from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, null=False,unique=True)
    age = models.IntegerField(null=True)  # 不能爲空
    sex = models.BooleanField(default='1')
