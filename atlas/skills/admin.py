# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Skill, Task, Days

admin.register(Skill, Task, Days)(admin.ModelAdmin)
