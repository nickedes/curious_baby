from django.db import models

# Create your models here.


class questions(models.Model):
    question = models.CharField(max_length=1000)
    qid = models.IntegerField(primary_key=True)

# class choices(models.Model):
