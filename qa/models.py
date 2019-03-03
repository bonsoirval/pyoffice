# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from crispy_forms.helper import FormHelper
#from django import forms


# Create your models here.
class Product_count(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places = 2,max_digits = 10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product_count_question(models.Model):
    product_count_question = models.CharField(max_length = 120)

    def __str__(self):
        return self.product_count_question

class Product_list_question(models.Model):
    product_list_question = models.CharField(max_length = 120)

    def __str__(self):
        return self.product_list_question

class Product(models.Model):
    name = models.CharField(max_length = 120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places = 2,max_digits = 10000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Manager_question(models.Model):
    manager_question = models.CharField(max_length = 120)

    def __str__(self):
        return self.manager_question


class Manager(models.Model):
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Lady', 'Lady'),
        ('Sir', 'Sir'),
    )
    title = models.CharField(max_length = 5, choices=TITLE_CHOICES, default = 'Mr')
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name

class Director_question(models.Model):
    director_question = models.CharField(max_length = 120)

    def __str__(self):
        return self.director_question

class Director(models.Model):
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Lady', 'Lady'),
        ('Sir', 'Sir'),
    )
    title = models.CharField(max_length = 5, choices=TITLE_CHOICES, default = 'Mr')
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name


class Number_of_staff(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.director_question

class Staff(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

    def __str__(self):
        return self.name

class Qa(models.Model):
    STUDENT_TYPE_CHOICES = (
        ('0', 'freshman'),
        ('1', 'sophomore'),
        ('2', 'junior'),
        ('3', 'senior'),
    )
    qa_question = models.CharField(max_length=100)
    qa_answer_sql = models.TextField()
    qa_answer_fucntion = models.CharField(max_length = 1, choices=STUDENT_TYPE_CHOICES, default = 'freshman')
    qa_created_at = models.DateField()

    def __str__(self):
        return self.qa_question

class Question(models.Model):
    QUESTION_FUNCTION_CHOICES = (
        ('0', 'director_question()'),
        ('1', 'manager_question()'),
        ('2', 'number_of_staff'),
        ('3', 'products_count'),
    )
    qa_question = models.CharField(max_length=100)
    qa_answer_sql = models.TextField()
    qa_function = models.CharField(max_length = 1, choices = QUESTION_FUNCTION_CHOICES, default = "Select Question Function")
    qa_created_at = models.DateField()

    def __str__(self):
        return self.qa_question
