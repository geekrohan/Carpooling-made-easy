# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-03-27 11:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20180128_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.CharField(choices=[('Car', 'Car'), ('Bike', 'Bike')], max_length=30, verbose_name='vehicle category'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{4}$', 32), 'Number Plate allowed in GJ01PM1234 format.', 'invalid')], verbose_name='liscenced plate number'),
        ),
    ]