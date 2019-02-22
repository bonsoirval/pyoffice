# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Qa, Question

# Register your models here.

admin.site.register(Qa),
admin.site.register(Question),
