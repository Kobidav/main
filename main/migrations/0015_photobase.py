# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_photobase'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sam_name', models.CharField(max_length=200, unique=True)),
                ('u_name', models.CharField(max_length=200)),
                ('so_name', models.CharField(max_length=200)),
                ('site_name', models.CharField(max_length=200)),
                ('url_name', models.CharField(max_length=1000)),
            ],
        ),
    ]
