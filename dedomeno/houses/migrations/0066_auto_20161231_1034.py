# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 09:34
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0065_auto_20161230_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='equipment',
        ),
        migrations.AddField(
            model_name='property',
            name='equipment',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=40, null=True), null=True, size=None),
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
    ]
