# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0014_auto_20170924_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applist',
            name='Appname',
            field=models.CharField(default='null', max_length=100, unique=True),
        ),
    ]