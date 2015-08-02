# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.forms import ModelForm
from .models import Skill, Task, Days


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('name',)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'completion_time',)


class DaysForm(ModelForm):
    class Meta:
        model = Days
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',)
