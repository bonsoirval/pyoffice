# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-03 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0017_auto_20190302_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Lady', 'Lady'), ('Sir', 'Sir')], default='Mr', max_length=5),
        ),
        migrations.AddField(
            model_name='question',
            name='qa_function',
            field=models.CharField(choices=[('0', 'director_question()'), ('1', 'manager_question()'), ('2', 'number_of_staff'), ('3', 'products_count')], default='Select Question Function', max_length=1),
        ),
    ]
