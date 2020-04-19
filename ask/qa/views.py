from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question_details(request, pk):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    return render(request, 'question_details.html', {'question': question, 'answers': answers})


def question_list(request):
    objects = Question.objects.new()
    limit = 10
    paginator = Paginator(objects, limit)
    page_number = request.GET.get('page', 1)
    questions = paginator.get_page(page_number)
    return render(request, 'index.html', {'questions': questions})

def popular_question_list(request):
    objects = Question.objects.popular()
    limit = 10
    paginator = Paginator(objects, limit)
    page_number = request.GET.get('page', 1)
    questions = paginator.get_page(page_number)
    return render(request, 'index.html', {'questions': questions})
