# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0056_auto_20161228_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='house',
            name='monthly_community_costs',
        ),
        migrations.RemoveField(
            model_name='house',
            name='transaction_type',
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='deposit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='monthly_community_costs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sourcehouse',
            name='transaction_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_transacion_house', to='houses.Transaction'),
        ),
    ]
