#-*- coding: utf-8 -*-

import os
import urllib
from django.shortcuts import render

# Create your views here.

from django.template import Context
from .models import Document

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.utils.encoding import smart_unicode

def roadmap(request):
	return render(request, 'roadmap/roadmap.html')

def document_intro(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	document = Document.objects.get(num=1)
	state = True
	files = document.filelist.split('/')
	if files[0] == '':
		state = False
	context = Context({'document': document, 'state': state, 'filename': files, 'size': range(0, len(files))})
	return render(request, 'document_intro.html', context)

def document_tools(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	document = Document.objects.get(num=2)
	context = Context({'document': document})
	return render(request, 'document_tools.html', context)

def document_collect(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	document = Document.objects.get(num=3)
	context = Context({'document': document})
	return render(request, 'document_collect.html', context)

def document_list(request):
	documents = Document.objects.order_by('num')
	context = Context({'documents': documents})
	return render(request, 'document_list.html', context)

@login_required(login_url='/login/')
def document_view(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	document_num = request.GET['dnum']
	document = Document.objects.get(num=document_num)
	state = True
	files = document.filelist.split('/')
	if files[0] == '':
		state = False
	context = Context({'document': document, 'state': state, 'filename': files, 'size': range(0, len(files))})
	return render(request, 'documents/' + str(document_num) + '.html', context)

@login_required(login_url='/login/')
def document_download(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	filename = request.GET['filename']
	if filename.find('/') != -1 or filename.find('..') != -1 or filename.find('.pdf') == -1:
		return HttpResponseRedirect('/')
	DOC_DIR = os.path.dirname(os.path.abspath(__file__))
	fp = open(os.path.join(DOC_DIR, 'document_file')+'/'+filename, 'r')
	response = StreamingHttpResponse(fp, content_type='application/force-download')
	if filename == 'intro1.pdf':
		filename_kor = '디지털_증거_수집_및_처리_등에_관한_규칙.pdf'
	elif filename == 'intro2.pdf':
		filename_kor = '디지털포렌식_수사관의_증거_수집_및_분석_규정.pdf'
	response['Content-Disposition'] = u'attachment; filename*=UTF-8\'\'%s' % urllib.quote(filename_kor)
	return response
