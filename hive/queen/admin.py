# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Abc,Message,MsgRecord,Token
# Register your models here.
admin.site.register(Token)
admin.site.register(Message)
admin.site.register(MsgRecord)
