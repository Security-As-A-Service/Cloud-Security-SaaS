# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0027_auto_20171002_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverlist',
            old_name='servname',
            new_name='servername',
        ),
    ]
