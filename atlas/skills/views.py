# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView, UpdateView

from braces.views import LoginRequiredMixin

# from .forms import UserForm
from .models import Skill, Task, Days


class SkillProgressView(LoginRequiredMixin, DetailView):
    pass


class SkillOverview(LoginRequiredMixin, UpdateView):
    pass


class SkillSetupView(LoginRequiredMixin, CreateView):
    pass


class SkillTodoView(LoginRequiredMixin, ListView):
    pass


def skillProgressView(request):
    #check my view yo
    return render(request, 'skills/skill_progress.html')


def skillOverview(request):
    #check my view yo
    return render(request, 'skills/skill_overview.html')


def skillSetupView(request):
    #check my view yo
    return render(request, 'skills/skill_setup.html')
