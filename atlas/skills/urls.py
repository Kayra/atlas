# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the SkillProgressView
    url(r'^$', views.skillProgressView, name='progress'),

    # URL pattern for the SkillOverview
    url(r'^overview/$', views.skillOverview, name='overview'),

    # URL pattern for the SkillSetupView
    url(r'^setup/$', views.skillSetupView, name='setup'),

    # URL pattern for the SkillListView
    url(r'^list/$', views.skillListView, name='list'),


    # API #####################################################################

    # Skills

    # URL pattern to create a skill
    url(r'^api/skill_create/$', views.skillCreate, name='skill_create'),

    # URL pattern to create a task
    url(r'^api/task_create/$', views.taskCreate, name='task_create'),

    # URL pattern to create a days
    url(r'^api/days_create/$', views.daysCreate, name='days_create'),

    # URL pattern to complete a listTask
    url(r'^api/listtask_complete/$', views.listTaskComplete, name='listTask_complete'),
]
