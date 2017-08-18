# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170818_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patch',
            name='is_enable',
        ),
        migrations.AddField(
            model_name='patch',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Wait'), (1, 'Online'), (2, 'Offline')], default=0),
        ),
    ]
