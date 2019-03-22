import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from data.models import Group, Current, Question, Answer


def index(request, group_name=''):
    group = Group.get(group_name)
    if group:
        return render(request, 'game/group.html', { 'group': group })
    return render(request, 'game/index.html')


def monitor(request):
    group_id = request.POST.get('group_id', 0)
    question_id = int(Current.get_value('question', 0))
    question = False
    answer = ''
    if question_id:
        question = Question.get(question_id)
        answer = Answer.get(question['id'], group_id)
    return JsonResponse({
        'question': question,
        'answer': answer
    })


def submit(request):
    group_id = request.POST.get('group_id', 0)
    question_id = request.POST.get('question_id', 0)
    submitted_answer = request.POST.get('answer', '')
    Answer.set(question_id, group_id, submitted_answer)
    return JsonResponse({
        'ok': 0
    })
