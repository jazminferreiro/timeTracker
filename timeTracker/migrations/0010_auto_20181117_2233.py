# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 22:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeTracker', '0009_auto_20181117_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='tareas',
        ),
        migrations.AddField(
            model_name='tarea',
            name='tareas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timeTracker.Proyecto'),
        ),
    ]
