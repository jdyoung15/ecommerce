# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180218_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
