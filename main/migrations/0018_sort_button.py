# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20161114_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sort_button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_field_name', models.CharField(max_length=200)),
                ('sort_field_value', models.CharField(max_length=200)),
                ('sort_sign', models.CharField(max_length=200)),
                ('sort_show_data', models.CharField(max_length=200)),
            ],
        ),
    ]
