# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20150820_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
