from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from .models import Question, Choice


def index(request):
    data = Question.objects.all()
    return render(request, 'polls/index.html', {'data':data})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {'question':question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error':"You did not select a choice"})
    else:
        selected_choice.vote +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html",{'question':question})

