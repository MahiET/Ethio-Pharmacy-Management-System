# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170304_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='contactno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
