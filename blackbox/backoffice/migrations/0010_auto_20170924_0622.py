# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0009_auto_20170915_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pentest',
            old_name='color',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='pentest',
            old_name='product',
            new_name='target',
        ),
        migrations.RemoveField(
            model_name='pentest',
            name='code',
        ),
        migrations.AddField(
            model_name='pentest',
            name='nbr_Day',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pentest',
            name='start_date',
            field=models.IntegerField(default=0),
        ),
    ]
