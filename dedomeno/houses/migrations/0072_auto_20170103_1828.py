# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0071_property_real_estate_raw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='property_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.Property'),
        ),
    ]
