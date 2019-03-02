# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-01 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0013_auto_20190301_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField()),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Products_question',
            new_name='Product_count_question',
        ),
        migrations.RenameField(
            model_name='product_questions',
            old_name='title',
            new_name='product_question',
        ),
        migrations.RemoveField(
            model_name='director',
            name='title',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product_questions',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product_questions',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='product_questions',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product_questions',
            name='summary',
        ),
    ]
