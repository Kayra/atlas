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

    # URL pattern to create a skill
    url(r'^api/create_skill/$', views.skillCreate, name='skill_create')

    # URL pattern to retrieve, update or delete a skill
    url(r'^api/detail_skill/(?P<pk>[0-9]+)/$', views.skillDetail, name='skill_detail')
]
