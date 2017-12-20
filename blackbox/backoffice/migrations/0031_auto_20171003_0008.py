# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0030_auto_20171003_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applist',
            name='Availibity',
            field=models.CharField(blank=True, choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], max_length=15),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Bamplus',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Bamplusid',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Confidentiality',
            field=models.CharField(blank=True, choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], max_length=15),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Developpment',
            field=models.CharField(blank=True, choices=[('INTERNAL', 'INTERNAL'), ('EXTERNAL', 'EXTERNAL'), ('SHARE', 'SHARE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Integrity',
            field=models.CharField(blank=True, choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], max_length=15),
        ),
        migrations.AlterField(
            model_name='applist',
            name='Tracability',
            field=models.CharField(blank=True, choices=[('4', 'EXTREME'), ('3', 'SERIOUS'), ('2', 'MODERATE'), ('1', 'LOW')], max_length=15),
        ),
        migrations.AlterField(
            model_name='applist',
            name='ciso_perim',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='applist',
            name='compliant_based_ident',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='fsa',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='fsa_level',
            field=models.CharField(blank=True, choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='gsf_lastdate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='applist',
            name='gsf_uptodate',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='https',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='n_tier',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='role_base_access_control',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='siem',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='ssl',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='tls',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5),
        ),
        migrations.AlterField(
            model_name='applist',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
