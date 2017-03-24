# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0073_property_price_raw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='real_estate',
        ),
        migrations.AddField(
            model_name='property',
            name='real_estate',
            field=models.ForeignKey(blank=True, help_text='If blank there is not a real estate involved', null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.RealEstate'),
        ),
    ]
