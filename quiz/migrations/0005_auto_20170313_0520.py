# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170313_0516'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testentries',
            unique_together=set([('attempt', 'question')]),
        ),
    ]
