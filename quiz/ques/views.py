from django.http import Http404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import questions, answer, choice


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

    elif request.GET.get('') is not None:
        return render_to_response('ques/change_choices.html')
    
    else:
        pop = request.GET['choice']
        obj = answer(qid=q, ansid=int(pop))
        obj.save()
        return render_to_response('ques/answer.html')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def add(request):
    if request.GET.get('question') is None:
        return render_to_response('ques/add.html')
    else:
        if request.GET.get('choice') is not None:
            # TODO: get the next qid for entry in db.
            latest_ques = questions.objects.order_by('qid').last()
            obj = questions(
                question=request.GET['question'], qid=latest_ques.qid+1)
            obj.save()
            # TODO: get cid for choice entry.
            latest_choice = choice.objects.order_by('cid').last()
            choice_obj = choice(
                cid=latest_choice.cid + 1, qid=obj,
                choice_text=request.GET['choice'], votes=0)
            choice_obj.save()
            return render_to_response('ques/add.html')


def modify(request, question_id):
    if request.GET.get('question') is None:
        return render_to_response('ques/modify.html')
    else:
        q = questions.objects.get(pk=question_id)
        q.question = request.GET['question']
        q.save()
        ques_avail = questions.objects.all()
        context = {'ques_avail': ques_avail}
        return render(request, 'ques/index.html', context)
