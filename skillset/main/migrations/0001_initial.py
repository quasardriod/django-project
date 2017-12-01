# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('user_pass', models.CharField(help_text='Use \'[algo]$[salt]$[hexdigest]\' or use the <a href="password/">change password form</a>.', max_length=10, verbose_name='password')),
                ('full_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]