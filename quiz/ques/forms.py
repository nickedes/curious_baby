from django import forms
from django.db import connection
# from .models import options
# from .models import questions


class OptionsForm(forms.Form):
    # print()
    cursor = connection.cursor()
    cursor.execute(
        "select choice_text, choice_text from ques_choice where qid_id = 1")
    CHOICES = cursor.fetchall()
    ans = forms.ChoiceField(choices=CHOICES)
