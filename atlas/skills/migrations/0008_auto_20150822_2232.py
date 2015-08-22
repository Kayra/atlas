# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0007_auto_20150822_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listtask',
            name='multiplier',
        ),
        migrations.AddField(
            model_name='listtask',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
