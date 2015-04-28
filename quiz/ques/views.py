from django.http import Http404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# from django.template import RequestContext, loader
from .models import questions, choice
from django.db import connection
# from .models import options
# from django import forms
# from .forms import OptionsForm


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
        cursor.execute("INSERT into ques_answer (qid_id, ansid) VALUES (%d,%d)" % (int(question_id) , int(pop)))
        # cursor.execute("INSERT into ques_answer (ansid,qid_id) VALUES (%d)" %int(question_id))

        return render_to_response('ques/ans.html')
        # cursor.execute('COMMIT')
        # return render(request, 'ques/detail.html', {'question': q})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# def response(request, choice_id):

#     return render(request, 'ques/response.html',{'c':choice_id})