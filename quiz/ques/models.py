from django.db import models

# Create your models here.


class questions(models.Model):
    question = models.CharField(max_length=1000)
    qid = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    qid = models.ForeignKey(questions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class options(models.Model):
    ans = models.CharField(max_length=200)
