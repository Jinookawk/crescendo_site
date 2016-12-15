#-*- coding: utf-8 -*-

import sys
import os
import urllib
from django.shortcuts import render

# Create your views here.

from django.template import Context
from .models import Notice
from .models import Freeboard, Comment_c
from .models import Community_scenario, Comment_scenario

from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseRedirect, StreamingHttpResponse

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

reload(sys)
sys.setdefaultencoding('utf-8')

class Counter:
	def __init__(self, num):
		self.count = num
	def decrease(self):
		self.count -= 1

def freeboard_list(request):
	data_num = Freeboard.objects.all().count()
	page_data = Paginator(Freeboard.objects.order_by('-num'), 5)
	page = request.GET.get('page', 1)

	try:
		freeboard_list = page_data.page(page)
	except PageNotAnInteger:
		freeboard_list = page_data.page(1)
	except EmptyPage:
		freeboard_list = page_data.page(page_data.num_pages)

	last_page = page_data.num_pages
	tcounter = Counter(data_num)
	context = Context({'request': request, 'freeboard_list': freeboard_list, 'current_page': int(page), 'total_page': range(1, page_data.num_pages + 1), 'last_page': last_page, 'counter': tcounter})
	return render(request, 'freeboard/freeboard_list.html', context)

def freeboard_view(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	freeboard_num = request.GET['fnum']
	freeboard = Freeboard.objects.get(num=freeboard_num)
	comments = Comment_c.objects.filter(freeboard_id=freeboard_num)
	state = False
	if request.user.is_staff or request.user.id == freeboard.author.id:
		state = True
	context = Context({'request': request, 'freeboard': freeboard, 'comments': comments, 'state': state})
	return render(request, 'freeboard/freeboard_view.html', context)

def freeboard_delete(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	freeboard_num = request.GET['fnum']
	freeboard = Freeboard.objects.get(num=freeboard_num)
	state = False
	if request.user.is_staff or request.user.id == freeboard.author.id:
		freeboard.delete()
		state = True
	context = Context({'state': state})
	return render(request, 'freeboard/freeboard_delete.html', context)

@login_required(login_url='/login/')
def freeboard_write(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	return render(request, 'freeboard/freeboard_write.html')

@login_required(login_url='/login/')
def freeboard_write_done(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	if request.method == "GET":
		return render(request, 'freeboard_write.html')
	if request.method == "POST":
		freeboard = Freeboard(title = request.POST['title'], author_id = request.user.id, content = request.POST['content'], f_comment_num = 0)
		freeboard.save()
	return render(request, 'freeboard/freeboard_write_done.html')

def comment_write_done(request):
	try:
		freeboard_num = request.GET['fnum']
		freeboard = Freeboard.objects.get(num=freeboard_num)
		comment_m = request.POST['message']
	except:
		return HttpResponseRedirect('/community/freeboard/list/')

	if comment_m is None:
		return HttpResponseRedirect('/')

	comment = Comment_c(freeboard_id = freeboard_num, author_id = request.user.id, message = comment_m)
	comment.save()

	Freeboard.objects.filter(num=freeboard_num).update(f_comment_num = freeboard.f_comment_num + 1)

	return HttpResponseRedirect('/community/freeboard/view/?fnum=' + freeboard_num)

def community_scenario_list(request):
	data_num = Community_scenario.objects.all().count()
	page_data = Paginator(Community_scenario.objects.order_by('-num'), 5)
	page = request.GET.get('page', 1)

	try:
		community_scenario_list = page_data.page(page)
	except PageNotAnInteger:
		community_scenario_list = page_data.page(1)
	except EmptyPage:
		community_scenario_list = page_data.page(page_data.num_pages)

	last_page = page_data.num_pages
	tcounter = Counter(data_num)
	context = Context({'request': request, 'community_scenario_list': community_scenario_list, 'current_page': int(page), 'total_page': range(1, page_data.num_pages + 1), 'last_page': last_page, 'counter': tcounter})
	return render(request, 'scenario/scenario_list.html', context)

def community_scenario_view(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	scenario_num = request.GET['scnum']
	community_scenario = Community_scenario.objects.get(num=scenario_num)
	comments = Comment_scenario.objects.filter(c_scenario_id=scenario_num)
	delete_state = False
	comment_state = False
	if request.user.is_staff or request.user.id == community_scenario.author.id:
		delete_state = True
		comment_state = True
	context = Context({'request': request, 'scenario': community_scenario, 'comments': comments, 'delete_state': delete_state, 'comment_state': comment_state, 'file_name': community_scenario.report_file})
	return render(request, 'scenario/scenario_view.html', context)

def community_scenario_delete(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	scenario_num = request.GET['scnum']
	community_scenario = Community_scenario.objects.get(num=scenario_num)
	state = False
	if request.user.is_staff or request.user.id == community_scenario.author.id:
		community_scenario.delete()
		state = True
	context = Context({'state': state})
	return render(request, 'scenario/scenario_delete.html', context)

def community_scenario_write(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	return render(request, 'scenario/scenario_write.html')

def community_scenario_write_done(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	if request.method == "GET":
		return render(request, 'scenario/scenario_write.html')
	if request.method == "POST":
		if 'reportfile' in request.FILES:
			file_r = request.FILES['reportfile']
			filename = file_r._name
			BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
			fp = open(os.path.join(BASE_DIR, 'media')+'/report/'+filename.encode('utf-8'), 'wb')
			for chunk in file_r.chunks():
				fp.write(chunk)
			fp.close()
			community_scenario = Community_scenario(title = request.POST['title'], author_id = request.user.id, report_file = unicode(filename), content = request.POST['content'], s_comment_num = 0)
			community_scenario.save()
	return render(request, 'scenario/scenario_write_done.html')

def s_comment_write_done(request):
	try:
		scenario_num = request.GET['scnum']
		community_scenario = Community_scenario.objects.get(num=scenario_num)
		comment_m = request.POST['message']
	except:
		return HttpResponseRedirect('/community/report/list/')

	if comment_m is None:
		return HttpResponseRedirect('/')

	comment = Comment_scenario(c_scenario_id = scenario_num, author_id = request.user.id, message = comment_m)
	comment.save()

	Community_scenario.objects.filter(num=scenario_num).update(s_comment_num = community_scenario.s_comment_num + 1)

	return HttpResponseRedirect('/community/report/view/?scnum=' + scenario_num)

def community_scenario_download(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	scenario_num = request.GET['scnum']
	community_scenario = Community_scenario.objects.get(num=scenario_num)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	fp = open(os.path.join(BASE_DIR, 'media')+'/report/'+community_scenario.report_file.encode('utf-8'), 'rb')
	response = StreamingHttpResponse(fp, content_type='application/force-download')
	response['Content-Disposition'] = u'attachment; filename*=UTF-8\'\'%s' % urllib.quote(community_scenario.report_file.encode('utf-8'))
	return response

def Noticelist(request):
	page_data = Paginator(Notice.objects.order_by('-num'), 5)
	page = request.GET.get('page', 1)

	if page is None:
		page = 1

	try:
		notice_list = page_data.page(page)
	except PageNotAnInteger:
		notice_list = page_data.page(1)
	except EmptyPage:
		notice_list = page_data.page(page_data.num_pages)

	last_page = page_data.num_pages
	context = Context({'request': request, 'notice_list': notice_list, 'current_page': int(page), 'total_page': range(1, page_data.num_pages + 1), 'last_page': last_page})
	return render(request, 'notice/notice_list.html', context)

def Noticeview(request):
	if not request.user.is_active:
		return HttpResponseRedirect('/login_check/')
	notice_num = request.GET['nnum']
	notice = Notice.objects.get(num=notice_num)
	Notice.objects.filter(num=notice_num).update(hits = notice.hits + 1)
	context = Context({'request': request, 'notice': notice})
	return render(request, 'notice/notice_view.html', context)

@login_required(login_url='/login/')
def Noticewrite(request):
	context = Context({})
	if not request.user.is_staff:
		return HttpResponseRedirect('/')
	return render(request, 'notice/notice_write.html', context)

def Noticewritedone(request):
	context = Context({})
	if not request.user.is_staff:
		return HttpResponseRedirect('/')
	if request.method == "GET":
		return render(request, 'notice/notice_write.html', context)
	if request.method == "POST":
		notice = Notice(title = request.POST['title'], created_date = datetime.now(), author_id = request.user.id, content = request.POST['content'], hits = 0)
		notice.save()
	return render(request, 'notice/notice_write_done.html', context)
