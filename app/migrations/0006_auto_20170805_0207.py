# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 02:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170805_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]