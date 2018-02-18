# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-18 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('reviewer_name', models.CharField(max_length=64)),
                ('rating', models.IntegerField()),
                ('review_content', models.TextField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
        ),
    ]
