# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_profile_picture_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture_url',
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
