
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Page(models.Model):
    Username = models.CharField(max_length=200)
    First_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



# Create your models here.
