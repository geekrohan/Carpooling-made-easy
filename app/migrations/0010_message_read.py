# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160715_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False, verbose_name='read'),
        ),
    ]
