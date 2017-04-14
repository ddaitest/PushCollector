# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def detail(request, abc):
    return HttpResponse("detail = %s"%abc)

def collect(request):
    return HttpResponse("OK")

def results(request, msg_id):
    return HttpResponse("results = %s"%msg_id)

def abc(request):
    return HttpResponse("OK ABC")
