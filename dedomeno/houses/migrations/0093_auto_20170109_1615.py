# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0092_office_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='houses.Property')),
                ('garage_type', models.CharField(blank=True, max_length=200, null=True)),
                ('garage_number', models.IntegerField(blank=True, null=True)),
                ('covered', models.NullBooleanField()),
                ('elevator', models.NullBooleanField()),
                ('automatic_door', models.NullBooleanField()),
                ('security_cameras', models.NullBooleanField()),
                ('alarm', models.NullBooleanField()),
                ('security_guard', models.NullBooleanField()),
            ],
            bases=('houses.property',),
        ),
        migrations.RenameField(
            model_name='house',
            old_name='garage',
            new_name='has_garage',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='garage',
            new_name='has_garage',
        ),
    ]
