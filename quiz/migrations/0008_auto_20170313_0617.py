# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_school_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='classes',
            field=models.ManyToManyField(to='quiz.Standard'),
        ),
    ]