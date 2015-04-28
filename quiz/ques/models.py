from django.db import models

# Create your models here.


class questions(models.Model):
    question = models.CharField(max_length=1000)
    qid = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.question

class answer(models.Model):
    qid = models.ForeignKey(questions, default=0)
    ansid = models.IntegerField()
    def __str__(self):
        return self.ansid

class choice(models.Model):
    cid = models.IntegerField(primary_key=True)
    qid = models.ForeignKey(questions)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
