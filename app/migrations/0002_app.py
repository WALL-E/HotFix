# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1024)),
                ('key', models.CharField(max_length=1024)),
                ('secret', models.CharField(max_length=1024)),
                ('rsa', models.CharField(max_length=1024)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('system_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.System')),
            ],
        ),
    ]