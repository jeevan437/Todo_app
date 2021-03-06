# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100, unique=True)),
                ('task_description', models.TextField()),
                ('task_status', models.CharField(choices=[('PARKED ', 'parked'), ('STARTED', 'started'), ('FINISHED', 'finished')], max_length=50)),
            ],
        ),
    ]
