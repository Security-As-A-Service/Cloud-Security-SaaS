# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0004_auto_20170914_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='criticity_level',
            field=models.IntegerField(choices=[('4', 'SERIOUS'), ('3', 'EXTREME'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
    ]
