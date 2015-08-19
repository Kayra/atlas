# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='times_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='times_listed',
            field=models.IntegerField(default=0),
        ),
    ]
