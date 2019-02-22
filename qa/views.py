"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'qa/index.html', {'title':"Intelligent Database Interface"})
"""

from django.shortcuts import render
from forms import MessageForm

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Database Interface"})
