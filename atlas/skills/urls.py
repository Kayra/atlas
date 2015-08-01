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

    # URL pattern for the SkillTodoView
    url(regex=r'^todo/$', view=views.SkillTodoView.as_view(), name='todo'),
]
