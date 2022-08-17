from typing import Optional
from django.shortcuts import render
from .models import Question, Choice


def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})


def vote(request, pk):
    questions = Question.objects.get(id=pk)
    options = questions.choices.all()
    # if request.method == 'POST':
    #     inputvalue = request.POST['choice']
    #     selected_option = options.get(id=inputvalue)
    #     selected_option.vote += 5
    #     selected_option.save()
    return render(request, 'vote.html', {'questions': questions, 'options': options})
    # return render(request, 'vote.html', {})


def result(request, pk):
    questions = Question.objects.get(id=pk)
    options = questions.choices.all()
    # optionsl = options.objects.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selected_option = options.get(id=inputvalue)
        selected_option.vote += 1
        # selected_option.vote1 = optionsl.get(id=inputvalue)
        selected_option.save()

    return render(request, 'result.html', {'questions': questions, 'options': options})


# def links(request, pk):
#     questions = Question.objects.get(id=pk)
#     options = questions.choices.all()
#     options1 = options.linksop.all()
#     if request.method == 'POST':
#         inputvalue = request.POST['choice']
#         selected_option = options1.get(id=inputvalue)
#         selected_option.vote += 5
#         selected_option.save()
#     #  return render(request, 'links.html', {'questions': questions, 'options': options})
#     return render(request, 'links.html', {'questions': questions, 'options': options, 'options1': options1})
