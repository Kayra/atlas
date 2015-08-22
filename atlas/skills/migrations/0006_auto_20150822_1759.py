# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_list_listtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
