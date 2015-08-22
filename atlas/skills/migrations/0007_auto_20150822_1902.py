# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_auto_20150822_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='friday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='monday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='saturday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='sunday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='thursday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='tuesday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='days',
            name='wednesday',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
