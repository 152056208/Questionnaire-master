# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20171205_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='take_part_num',
            field=models.IntegerField(default=0, verbose_name='参与人数'),
        ),
    ]
