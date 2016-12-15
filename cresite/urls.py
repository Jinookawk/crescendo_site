"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from .views import home

from .views import user_login, login_check, register_page, register_done
from .views import my_password_change, my_password_change_done
from .views import intro, documents, problems, community, mypage, rank_page
from community.views import Noticelist, Noticeview, Noticewrite, Noticewritedone

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^login/$', user_login, name='user_login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^login_check/$', login_check, name='login_check'),
	url(r'^register/$', register_page, name='register_page'),
	url(r'^register/done/$', register_done, name='register_done'),
	url(r'^mypage/password_change/$', my_password_change, name='password_change'),
	url(r'^mypage/password_change/done/$', my_password_change_done, name='password_change_done'),

	#url(r'^accounts/', include('django.contrib.auth.urls')),
	
	url(r'^$', home, name='home'),

	url(r'^intro/$', intro, name='intro'),
	# url(r'^documents/$', documents, name='documents'),
	url(r'^documents/', include('document.urls')),
	# url(r'^problems/$', problems, name='problems'),
	url(r'^problems/', include('problem.urls')),
	# url(r'^community/$', community, name='community'),
	url(r'^community/', include('community.urls')),
	url(r'^question/', include('question.urls')),

	url(r'^notice/list/$', Noticelist, name='noticelist'),
	url(r'^notice/view/$', Noticeview, name='noticeview'),
	url(r'^notice/write/$', Noticewrite, name='noticewrite'),
	url(r'^notice/write/done/$', Noticewritedone, name='noticewritedone'),

	url(r'^mypage/$', mypage, name='mypage'),
	url(r'^rank/$', rank_page, name='rank_page'),
]
