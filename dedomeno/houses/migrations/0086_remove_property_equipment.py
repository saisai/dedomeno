# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0085_auto_20170108_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='equipment',
        ),
    ]
