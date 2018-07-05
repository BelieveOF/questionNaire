from django.db import models
from user.models import User
# Create your models here.


class Questionnaires(models.Model):
    title=models.CharField(max_length=300,null=False)
    creator=models.ForeignKey(User)
    questionnaire_type=models.CharField(max_length=50)
    create_time=models.DateTimeField(auto_now_add=True)

    clicks = models.IntegerField(default=0)
    def all_question(self):
        return self.questions_set.all()

class Questions(models.Model):
    name=models.CharField(max_length=300,null=False)
    questionnaire=models.ForeignKey(Questionnaires)
    single_selection=models.BooleanField(default=True)


    def all_option(self):
        return self.options_set.all()


class Options(models.Model):
    name=models.CharField(max_length=50,null=False)
    question=models.ForeignKey(Questions)
