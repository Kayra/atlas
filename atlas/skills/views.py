# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SkillSerializer, TaskSerializer, DaysSerializer

from .models import Skill, Task, Days

from .utility import allTasks

from .progress import *

from .list import *


# Pull all tasks for user
# Pull all skills for user
# Run progress utility methods
# Return object and pass it to the template to be displayed
@login_required
def skillProgressView(request):

    user = request.user

    skills = Skill.objects.filter(user=user)
    skillStats = []

    for skill in skills:
        tasks = Task.objects.filter(skill=skill)
        skillStats.append(Progress(tasks))

    return render(request, 'skills/skill_progress.html', {
        'skills': skillStats,
        })


# Pull all tasks for user
# Pull all skills for user
# Pass them to the template to be displayed
@login_required
def skillOverview(request):

    user = request.user

    try:
        # Check if the user already has a skill
        Skill.objects.filter(user=user)[0]

        skills = Skill.objects.filter(user=user)

        tasks = allTasks(user)

        days = Days.objects.get(user=user)

        return render(request, 'skills/skill_overview.html', {
            'skills': skills,
            'tasks': tasks,
            'days': days,
        })

    except IndexError:
        return redirect('skills:setup')


@login_required
def skillSetupView(request):

    """
    Render the page that will allow the user to save one skill, multiple tasks and all the days. If the user has already registered a skill, redirect them to the overview page.
    """

    user = request.user

    try:
        # Check if the user already has a skill
        Skill.objects.filter(user_id=user.id)[0]
        return redirect('skills:overview')

    except IndexError:
        if request.method == 'POST':
            return redirect('skills:overview')
        return render(request, 'skills/skill_setup.html')


# Pull all tasks for user
# Run list utility methods
# Return dictionary containing tasks and times to be displayed
@login_required
def skillListView(request):

    try:
        List.objects.get(date=datetime.now())
        tasks = ListTask.objects.filter(list__date=datetime.now()).order_by('position')

    except List.DoesNotExist:
        createList(request.user)
        tasks = ListTask.objects.filter(list__date=datetime.now()).order_by('position')

    return render(request, 'skills/skill_list.html', {
        'list': tasks,
    })


# API #########################################################################

@api_view(['POST'])
def skillCreate(request):

    serializer = SkillSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)
    serializer.initial_data['skill'] = Skill.objects.filter(name=serializer.initial_data['skill'])[:1]

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def daysCreate(request):

    serializer = DaysSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def listTaskComplete(request):

    listTask = ListTask.objects.get(id=request.data['id'])
    listTask.completed = request.data['completed']
    listTask.save()

    task = Task.objects.get(name=listTask.name, skill__user=request.user)
    task.times_completed += 1
    task.save()

    return Response(request.data, status=status.HTTP_201_CREATED)
