# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Qa, Question , \
Product, Product_questions, Manager_question, Manager, \
Director_question, Director, Number_of_staff, Staff, \
Product_questions,Product, Products_question

# Register your models here.

admin.site.register(Qa),
admin.site.register(Question),
admin.site.register(Product),
admin.site.register(Manager_question),
admin.site.register(Manager),
admin.site.register(Director_question),
admin.site.register(Director),
admin.site.register(Number_of_staff),
admin.site.register(Staff),
admin.site.register(Products_question),
admin.site.register(Product_questions),
