# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from datetime import timedelta

from django.db import models
from atlas.users.models import User
# from django.utils.translation import ugettext_lazy as _


class Skill(models.Model):

    name                = models.CharField("Skill name", max_length=255)

    user                = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class Task(models.Model):

    name                = models.CharField("Task name", max_length=255)
    completion_time     = models.DurationField(default=timedelta())
    times_listed        = models.IntegerField(default=0)
    times_completed     = models.IntegerField(default=0)

    skill               = models.ForeignKey(Skill)

    def __unicode__(self):
        return self.name


class Days(models.Model):

    monday              = models.DurationField(default=timedelta())
    tuesday             = models.DurationField(default=timedelta())
    wednesday           = models.DurationField(default=timedelta())
    thursday            = models.DurationField(default=timedelta())
    friday              = models.DurationField(default=timedelta())
    saturday            = models.DurationField(default=timedelta())
    sunday              = models.DurationField(default=timedelta())

    user                = models.ForeignKey(User)


class List(models.Model):

    date                = models.DateField(auto_now_add=True)

    user                = models.ForeignKey(User)


class ListTask(models.Model):

    name                = models.CharField("Task name", max_length=255)
    completion_time     = models.DurationField(default=timedelta())
    position            = models.IntegerField(null=True)
    completed           = models.BooleanField(default=False)

    list                = models.ForeignKey(List)
