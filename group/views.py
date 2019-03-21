import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from data.models import Group, Current, Question

# Create your views here.
def index(request, group_name=''):
    group = Group.get(group_name)
    question = Current.get_value('question')
    if question:
        question = Question.get(question)
    data = { 'group': group, 'question': question }
    return render(request, 'group/index.html', data)
