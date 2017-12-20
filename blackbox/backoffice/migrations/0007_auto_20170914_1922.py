# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0006_auto_20170914_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Availibity',
            field=models.CharField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Confidentiality',
            field=models.CharField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Integrity',
            field=models.CharField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0, max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='Tracability',
            field=models.CharField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0, max_length=15),
        ),
    ]
