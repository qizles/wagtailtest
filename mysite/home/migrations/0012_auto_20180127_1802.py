# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20180127_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='card1symbol',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card2symbol',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='homepage',
            name='card3symbol',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]