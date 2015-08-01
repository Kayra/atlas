# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

# from .forms import UserForm
from .models import Skill, Task, Days


def skillProgressView(request):
    #check my view yo
    return render(request, 'skills/skill_progress.html')


def skillOverview(request):
    #check my view yo
    return render(request, 'skills/skill_overview.html')


def skillSetupView(request):
    #check my view yo
    return render(request, 'skills/skill_setup.html')

def skillListView(request):
    #check my view yo
    return render(request, 'skills/skill_list.html')

