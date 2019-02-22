# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from crispy_forms.helper import FormHelper
from django import forms


# Create your models here.
class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        self.helper  = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

class Qa(models.Model):
    qa_question = models.CharField(max_length=100)
    qa_answer_sql = models.TextField()
    qa_created_at = models.DateField()

class Question(models.Model):
    qa_question = models.CharField(max_length=100)
    qa_answer_sql = models.TextField()
    qa_created_at = models.DateField()

    def __str__(self):
        return self.qa_question
