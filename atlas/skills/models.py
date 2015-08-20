# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

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
    completion_time     = models.DurationField()
    times_listed        = models.IntegerField(default=0)
    times_completed     = models.IntegerField(default=0)

    skill               = models.ForeignKey(Skill)

    def __unicode__(self):
        return self.name


class Days(models.Model):

    monday              = models.TimeField()
    tuesday             = models.TimeField()
    wednesday           = models.TimeField()
    thursday            = models.TimeField()
    friday              = models.TimeField()
    saturday            = models.TimeField()
    sunday              = models.TimeField()

    user                = models.ForeignKey(User)
