# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Abc(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Message(models.Model):
    #is_notification
    #expied_on
    #platform
    title = models.CharField(max_length=200)
    cotent = models.CharField(max_length=200)
    created_on = models.DateTimeField('created')
    def __str__(self):
        return self.title

@python_2_unicode_compatible  # only if you need to support Python 2
class MsgRecord(models.Model):
    msg = models.ForeignKey(Message, on_delete=models.CASCADE) 
    plaform = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    sent_on = models.DateTimeField('sent')
    reach_on = models.DateTimeField('reach')
    def __str__(self):
        return self.token

@python_2_unicode_compatible  # only if you need to support Python 2
class Token(models.Model):
    token = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    
    def __str__(self):
        return self.token