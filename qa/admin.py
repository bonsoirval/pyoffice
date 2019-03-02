# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Qa, Question , \
Product, Product_list_question, Product_count_question, Manager_question, Manager, \
Director_question, Director, Number_of_staff, Staff, \
Product

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
admin.site.register(Product_list_question),
admin.site.register(Product_count_question),
