# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20150819_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_time',
            field=models.DurationField(),
        ),
    ]
