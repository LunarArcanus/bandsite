# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('est_date', models.DateTimeField(verbose_name='date established')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('members', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='BandVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.BandInfo')),
            ],
        ),
    ]
