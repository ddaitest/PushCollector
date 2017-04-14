# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Abc,Message,MsgRecord
# Register your models here.
admin.site.register(Abc)
admin.site.register(Message)
#admin.site.register(MsgRecord)
