# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20170315_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='testentries',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='testentries',
            name='answer',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]