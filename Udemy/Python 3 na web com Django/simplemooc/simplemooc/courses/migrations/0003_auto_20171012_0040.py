# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20171012_0027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='strat_date',
            new_name='start_date',
        ),
    ]
