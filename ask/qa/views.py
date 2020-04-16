from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def question_details(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    return render(reauest, 'question_details.html', {'question': question, 'answers': answers})

def question_list(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    page.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


def popular_question_list(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    page.baseurl = '/popular/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


#def question_list(request):
 #   objects = Question.objects.new()
  #  limit = 10
   # paginator = Paginator(objects, limit)
    #page_number = request.GET.get('page', 1)
    #questions = paginator.get_page(page_number)
    #return render(request, 'index.html', {'questions': questions})

#def popular_question_list(request):
 #   objects = Question.objects.popular()
  #  limit = 10
   # paginator = Paginator(objects, limit)
    #page_number = request.GET.get('page', 1)
    #questions = paginator.get_page(page_number)
    #return render(request, 'index.html', {'questions': questions})
