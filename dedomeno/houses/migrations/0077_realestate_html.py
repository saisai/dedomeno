# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0076_auto_20170104_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='html',
            field=models.TextField(blank=True, null=True),
        ),
    ]