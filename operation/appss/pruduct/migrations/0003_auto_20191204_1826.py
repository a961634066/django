# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-04 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruduct', '0002_auto_20191204_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='\u540d\u79f0'),
        ),
    ]
