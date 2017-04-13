# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Message(models.Model):
    title = models.CharField(max_length=200)
    cotent = models.CharField(max_length=200)
    created_on = models.DateTimeField('created on')

class MsgRecord(models.Model):
    msg = models.ForeignKey(Message, on_delete=models.CASCADE) 
    plaform = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    sent_on = models.DateTimeField('sent on')
    reach_on = models.DateTimeField('reach on')
