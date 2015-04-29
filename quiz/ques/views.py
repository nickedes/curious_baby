from django.http import Http404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import questions, choice
from django.db import connection


def index(request):
    ques_avail = questions.objects.all()
    context = {'ques_avail': ques_avail}
    return render(request, 'ques/index.html', context)


def detail(request, question_id):
    # form = OptionsForm(request.POST or None)
    try:
        q = questions.objects.get(pk=question_id)
    except questions.DoesNotExist:
        raise Http404("Question does not exist")
    if request.GET.get('choice') is None:
        return render(request, 'ques/detail.html', {'question': q})
    else:
        pop = request.GET.get('choice')
        print(question_id)
        cursor = connection.cursor()
        cursor.execute("INSERT into ques_answer (qid_id, ansid) VALUES (%d,%d)" % (
            int(question_id), int(pop)))
        return render_to_response('ques/answer.html')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
