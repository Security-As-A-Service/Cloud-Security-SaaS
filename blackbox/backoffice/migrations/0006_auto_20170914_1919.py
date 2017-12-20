# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0005_auto_20170914_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Availibity',
            field=models.IntegerField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Confidentiality',
            field=models.IntegerField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Integrity',
            field=models.IntegerField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Tracability',
            field=models.IntegerField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='criticity_level',
            field=models.IntegerField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sensitivity_level',
            field=models.CharField(choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], default='null', max_length=10),
        ),
    ]