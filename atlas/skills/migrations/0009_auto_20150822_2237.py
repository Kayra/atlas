# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0008_auto_20150822_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtask',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]
