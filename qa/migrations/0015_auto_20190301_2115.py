# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-01 21:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0014_auto_20190301_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
