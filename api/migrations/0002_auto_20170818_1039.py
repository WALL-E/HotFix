# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category'},
        ),
        migrations.AlterModelOptions(
            name='system',
            options={'verbose_name': 'system'},
        ),
    ]
