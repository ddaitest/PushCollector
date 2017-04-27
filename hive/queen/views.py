# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Message, MsgRecord
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from pms import pm

# Create your views here.
def index(request):
    msg_list = Message.objects.order_by('created_on')[:5]
    context = {'msg_list': msg_list}
    return render(request, 'queen/index.html', context)

def detail(request, abc):
    try:
        msg = Message.objects.get(pk=abc)
    except Message.DoesNotExist:
        raise Http404("Message does not exist")
    return render(request, 'queen/detail.html', {'msg': msg})

def collect(request):
    return HttpResponse("123 Collect OK")

def write(request):
    return render(request, 'queen/write.html')

@csrf_exempt
def send(request):
    log = pm.push(request.POST)
    return render(request, 'queen/send.html', {'send_list': log})
    #return HttpResponse(log)

@csrf_exempt
def register(request):
    log = pm.register(request.POST)
    return HttpResponse(log)

def home(request):
	return render(request, 'queen/home.html', {})
