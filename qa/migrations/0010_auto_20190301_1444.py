# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-01 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0009_auto_20190301_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='title',
            field=models.CharField(choices=[('mr', 'Mr'), ('1', 'Sir'), ('2', 'Mrs'), ('3', 'Lady')], default='Mr', max_length=1),
        ),
    ]
