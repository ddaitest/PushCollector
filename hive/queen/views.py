# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Message, MsgRecord

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
	return HttpResponse("Collect OK")

def write(request):
	return render(request, 'queen/write.html')

def send(request):
	title = request.POST['title']
	content = request.POST['content']
	return HttpResponse("OK :"+title+content)
