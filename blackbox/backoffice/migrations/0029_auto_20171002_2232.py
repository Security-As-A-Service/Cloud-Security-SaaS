# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0028_auto_20171002_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverlist',
            name='os',
            field=models.CharField(choices=[('Windows', 'Windows'), ('Unix', 'Unix'), ('Linux', 'Linux'), ('Macintosh', 'Macintosh')], max_length=100),
        ),
    ]
