# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-19 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Addresse éléctronique')),
                ('first_name', models.CharField(max_length=30, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=30, verbose_name='Nom')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Numéro de téléphone')),
                ('civility', models.CharField(choices=[('M', 'Monsieur'), ('Mme', 'Madame'), ('Mlle', 'Mademoiselle')], max_length=4)),
                ('marital_status', models.CharField(choices=[('Célibataire', 'Célibataire'), ('Marié(e)', 'Marié(e)'), ('Veuf(ve)', 'Veuf(ve)'), ('Divorcé(e)', 'Divorcé(e)')], max_length=250)),
                ('birthday', models.DateField()),
                ('postcode', models.CharField(max_length=250)),
                ('profession', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('address_2', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('social_security_number', models.CharField(max_length=255)),
                ('social_security_organism_name', models.CharField(max_length=255)),
                ('social_security_organism_code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
