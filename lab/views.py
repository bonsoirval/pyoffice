# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__  import absolute_import

from django.shortcuts import render

# Create your views here.
from django.views import generic
#from django.contrib.auth.forms import UserCreationForm
from . forms import RegistrationForm
from django.contrib.auth.models import User

class HomePageView(generic.TemplateView):
    template_name = 'home.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'signup.html'
