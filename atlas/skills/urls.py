# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the SkillProgressView
    url(regex=r'^$', view=views.SkillProgressView.as_view(), name='progress'),

    # URL pattern for the SkillOverview
    url(regex=r'^overview/$', view=views.SkillOverview.as_view(), name='overview'),

    # URL pattern for the SkillSetupView
    url(regex=r'^setup/$', view=views.SkillSetupView.as_view(), name='setup'),

    # URL pattern for the SkillTodoView
    url(regex=r'^todo/$', view=views.SkillTodoView.as_view(), name='todo'),
]
