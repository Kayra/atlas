# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

# from .forms import UserForm
from .models import Skill, Task, Days


def skillProgressView(request):
    # Pull all tasks for user
    # Pull all skills for user
    # Run progress utility methods
    # Return object and pass it to the template to be displayed
    return render(request, 'skills/skill_progress.html')


def skillOverview(request):
    # Pull all tasks for user
    # Pull all skills for user
    # Pass them to the template to be displayed
    return render(request, 'skills/skill_overview.html')


def skillSetupView(request):
    # Save one skill for user
    # Save multiple tasks for user
    return render(request, 'skills/skill_setup.html')

def skillListView(request):
    # Pull all tasks for user
    # Run list utility methods
    # Return dictionary containing tasks and times to be displayed
    return render(request, 'skills/skill_list.html')
