# -*- coding: utf-8 -*-
# Generated by Django 1.10.1
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercompany', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='companystock',
            table='company_stock',
        ),
    ]