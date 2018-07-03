from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userinfo(models.Model):
    """

    """
    # user models.OneToOneField(User,help_text='普通用户')
    # pass
    username = models.CharField(max_length=150,null=False)
    age = models.IntegerField(null=False)  # 不能爲空
    sex = models.BooleanField(null=False)
    passwd = models.CharField(max_length=256)



# class Questionnaire(models.Model):
    # customer=models.ForeignKey()
    # pass
