# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0055_auto_20161228_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcehouse',
            name='page',
            field=models.TextField(blank=True, null=True),
        ),
    ]
