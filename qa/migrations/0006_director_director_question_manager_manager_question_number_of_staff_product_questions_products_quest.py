# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-25 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20190222_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_question', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_question', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Number_of_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField()),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_question', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
    ]
