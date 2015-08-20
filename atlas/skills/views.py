# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SkillSerializer, TaskSerializer, DaysSerializer

from .models import Skill, Task, Days

from .progress import *


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

    skills = Skill.objects.filter(user=user)

    tasks = []
    for skill in skills:
        skillTasks = Task.objects.filter(skill=skill)
        for task in skillTasks:
            tasks.append(task)

    days = Days.objects.get(user=user)

    return render(request, 'skills/skill_overview.html', {
        'skills': skills,
        'tasks': tasks,
        'days': days,
    })


@login_required
def skillSetupView(request):

    """
    Render the page that will allow the user to save one skill, multiple tasks and all the days. If the user has already registered a skill, redirect them to the overview page.
    """

    currentUser = request.user

    try:
        # Check if the user already has a skill
        Skill.objects.filter(user_id=currentUser.id)[0]
        return redirect('skills:overview')

    except IndexError:
        if request.method == 'POST':
            return redirect('skills:overview')
        return render(request, 'skills/skill_setup.html')


@login_required
def skillListView(request):

    # Pull all tasks for user
    # Run list utility methods
    # Return dictionary containing tasks and times to be displayed
    return render(request, 'skills/skill_list.html')


# API #########################################################################

@api_view(['POST'])
def skillCreate(request):

    serializer = SkillSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def skillDetail(request, pk):

    """
    Retrieve, update or delete a skill.
    """

    try:
        skill = Skill.objects.get(pk=pk)
    except Skill.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SkillSerializer(skill, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)
    serializer.initial_data['skill'] = Skill.objects.filter(name=serializer.initial_data['skill'])[:1]

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def taskDetail(request, pk):

    """
    Retrieve, update or delete a task.
    """

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def daysCreate(request):

    serializer = DaysSerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
