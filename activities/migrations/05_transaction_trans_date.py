s (16 sloc)  490 Bytes

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '04_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='trans_date',
            field=models.DateField(default=datetime.date(2017, 5, 1)),
        ),
    ]
