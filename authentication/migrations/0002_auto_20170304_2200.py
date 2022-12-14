# -*- coding: utf-8 -*-
# Generated by Django 1.10.1
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(max_length=10)),
                ('contactno', models.IntegerField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='license_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.CharField(blank=True, choices=[('S', 'Shop'), ('C', 'Company')], max_length=1),
        ),
        migrations.AlterModelTable(
            name='profile',
            table='inst_profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.Address'),
        ),
    ]
