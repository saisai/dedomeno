# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0070_auto_20170103_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='real_estate_raw',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
