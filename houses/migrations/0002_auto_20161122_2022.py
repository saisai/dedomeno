# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyLocalization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ComunidadAutonoma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MunicipioArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('comunidad_autonoma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.ComunidadAutonoma')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Provincia')),
            ],
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_area',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_comunidad',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_municipio',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_number',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_postal_code',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_province',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_street',
        ),
        migrations.RemoveField(
            model_name='house',
            name='address_zona',
        ),
        migrations.RemoveField(
            model_name='house',
            name='elevator',
        ),
        migrations.RemoveField(
            model_name='house',
            name='is_owner_real_state',
        ),
        migrations.RemoveField(
            model_name='house',
            name='transaction',
        ),
        migrations.AddField(
            model_name='agency',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='monthly_community_costs',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='transaction_type',
            field=models.CharField(choices=[('rent', 'rent'), ('buy', 'buy')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='agency',
            field=models.ForeignKey(blank=True, help_text='If blank there is not an agency involved', on_delete=django.db.models.deletion.CASCADE, to='houses.Agency'),
        ),
        migrations.AlterField(
            model_name='house',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='conditions',
            field=models.CharField(blank=True, choices=[('good', 'good'), ('bad', 'bad')], max_length=2),
        ),
        migrations.AlterField(
            model_name='house',
            name='deposit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='energy_label',
            field=models.CharField(blank=True, choices=[('A+++', 'A+++'), ('A++', 'A++'), ('A+', 'A+'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('No', 'No')], default='No', max_length=4),
        ),
        migrations.AlterField(
            model_name='house',
            name='equipment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='houses.Equipment'),
        ),
        migrations.AlterField(
            model_name='house',
            name='flat_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='flat_num_total',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='house_type',
            field=models.CharField(blank=True, choices=[('flat', 'piso'), ('house', 'chalet'), ('rustic', 'rustico'), ('duplex', 'duplex'), ('attic', 'atico')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='m2_to_use',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='m2_total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='orientation',
            field=models.CharField(blank=True, choices=[('N', 'N'), ('NE', 'NE'), ('E', 'E'), ('S', 'S'), ('SW', 'SW'), ('W', 'W'), ('NW', 'NW')], max_length=2),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner_phone',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.Source'),
        ),
        migrations.AlterField(
            model_name='house',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='municipioarea',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Zona'),
        ),
        migrations.AddField(
            model_name='comunidadautonoma',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Country'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='municipio_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.MunicipioArea'),
        ),
        migrations.AddField(
            model_name='agencylocalization',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Agency'),
        ),
        migrations.AddField(
            model_name='agencylocalization',
            name='barrio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.Barrio'),
        ),
        migrations.AddField(
            model_name='agency',
            name='agency_localization',
            field=models.ManyToManyField(through='houses.AgencyLocalization', to='houses.Barrio'),
        ),
        migrations.AddField(
            model_name='house',
            name='barrio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.Barrio'),
        ),
    ]