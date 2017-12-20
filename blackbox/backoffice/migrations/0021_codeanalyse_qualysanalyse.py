# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0020_auto_20170924_2354'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeAnalyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nbr_Day', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('auditor', models.CharField(choices=[('BF', 'Beijaflore'), ('Nes', 'Nes'), ('Gfi', 'Gfi'), ('ISPL', 'ISPL'), ('AST', 'AppSecTeam')], default='null', max_length=15)),
                ('pilote', models.CharField(choices=[('dla', 'Damien Lallement'), ('ala', 'Alexandre Lasnier'), ('...', '...')], default='null', max_length=15)),
                ('total_vulnerability', models.IntegerField(default=0)),
                ('critical_vulnerability', models.IntegerField(default=0)),
                ('high_vulnerability', models.IntegerField(default=0)),
                ('medium_vulnerability', models.IntegerField(default=0)),
                ('low_vulnerability', models.IntegerField(default=0)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.AppList')),
            ],
        ),
        migrations.CreateModel(
            name='QualysAnalyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nbr_Day', models.IntegerField(default=0)),
                ('start_date', models.DateTimeField()),
                ('auditor', models.CharField(choices=[('BF', 'Beijaflore'), ('Nes', 'Nes'), ('Gfi', 'Gfi'), ('ISPL', 'ISPL'), ('AST', 'AppSecTeam')], default='null', max_length=15)),
                ('pilote', models.CharField(choices=[('dla', 'Damien Lallement'), ('ala', 'Alexandre Lasnier'), ('...', '...')], default='null', max_length=15)),
                ('total_vulnerability', models.IntegerField(default=0)),
                ('critical_vulnerability', models.IntegerField(default=0)),
                ('high_vulnerability', models.IntegerField(default=0)),
                ('medium_vulnerability', models.IntegerField(default=0)),
                ('low_vulnerability', models.IntegerField(default=0)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backoffice.AppList')),
            ],
        ),
    ]