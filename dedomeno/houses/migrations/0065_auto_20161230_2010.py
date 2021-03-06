# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0064_auto_20161230_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=10000, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('source_id', models.CharField(blank=True, max_length=200, null=True)),
                ('source_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='agency',
            name='agency_localization',
        ),
        migrations.RemoveField(
            model_name='agencylocalization',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='agencylocalization',
            name='place',
        ),
        migrations.RemoveField(
            model_name='agencylocalizationsource',
            name='agency_localization',
        ),
        migrations.RemoveField(
            model_name='agencylocalizationsource',
            name='source',
        ),
        migrations.RemoveField(
            model_name='source',
            name='agency_location_source',
        ),
        migrations.RemoveField(
            model_name='source',
            name='territorial_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='transaction_url',
        ),
        migrations.RemoveField(
            model_name='sourceproperty',
            name='agency_location_source',
        ),
        migrations.RemoveField(
            model_name='sourceproperty',
            name='property_item',
        ),
        migrations.RemoveField(
            model_name='sourceproperty',
            name='source',
        ),
        migrations.RemoveField(
            model_name='sourceproperty',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='sourcetransaction',
            name='source',
        ),
        migrations.RemoveField(
            model_name='sourcetransaction',
            name='transaction',
        ),
        migrations.RemoveField(
            model_name='territorialentity',
            name='country',
        ),
        migrations.RemoveField(
            model_name='territorialentity',
            name='father',
        ),
        migrations.RemoveField(
            model_name='territorialentity',
            name='near_brothers',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='father',
        ),
        migrations.RemoveField(
            model_name='urlsourceterritory',
            name='source',
        ),
        migrations.RemoveField(
            model_name='urlsourceterritory',
            name='territory',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='equipment_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='house',
            name='conditions',
        ),
        migrations.RemoveField(
            model_name='house',
            name='flat_num_total',
        ),
        migrations.RemoveField(
            model_name='property',
            name='source_property',
        ),
        migrations.RemoveField(
            model_name='property',
            name='territorial_entity',
        ),
        migrations.AddField(
            model_name='house',
            name='good_condition',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='property',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='html',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='offline_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='online_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='phone_1',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='phone_2',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='source',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='transaction',
            field=models.CharField(blank=True, choices=[('rent', 'sale'), ('sale', 'sale')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.DeleteModel(
            name='AgencyLocalization',
        ),
        migrations.DeleteModel(
            name='AgencyLocalizationSource',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='SourceProperty',
        ),
        migrations.DeleteModel(
            name='SourceTransaction',
        ),
        migrations.DeleteModel(
            name='TerritorialEntity',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='URLSourceTerritory',
        ),
        migrations.AddField(
            model_name='property',
            name='agency',
            field=models.ManyToManyField(blank=True, help_text='If blank there is not a real estate involved', to='houses.RealEstate'),
        ),
    ]
