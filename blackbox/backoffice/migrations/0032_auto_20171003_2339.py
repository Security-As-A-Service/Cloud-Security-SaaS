# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0031_auto_20171003_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applist',
            name='gsf_lastdate',
            field=models.DateTimeField(),
        ),
    ]
