# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apacskills', '0003_auto_20171207_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills_map',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
