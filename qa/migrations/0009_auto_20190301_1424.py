# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-01 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0008_manager_qa_answer_fucntion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='qa_answer_fucntion',
            new_name='title',
        ),
    ]