# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
