from django.http import Http404
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
# from django.template import RequestContext, loader
from .models import questions
from django.db import connection
from .models import options
from django import forms
# from .forms import OptionsForm


def index(request):
    ques_avail = questions.objects.all()
    context = {'ques_avail': ques_avail}
    return render(request, 'ques/index.html', context)


def detail(request, question_id):
    # form = OptionsForm(request.POST or None)
    try:
        q = questions.objects.get(pk=question_id)
        print(question_id)
        cursor = connection.cursor()
        cursor.execute(
            "select choice_text from ques_choice where qid_id = %s",[question_id])
        CHOICES = cursor.fetchall()
        print(CHOICES)
        ans = forms.ChoiceField(choices=CHOICES)
    except questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'ques/detail.html', {'question': q, 'form': ans})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
