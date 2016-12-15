from django.conf.urls import url
from .views import Noticelist
from .views import Noticeview
from .views import Noticewrite
from .views import Noticewritedone
from .views import freeboard_list
from .views import freeboard_view
from .views import freeboard_write
from .views import freeboard_write_done
from .views import comment_write_done
from .views import freeboard_delete
from .views import community_scenario_list, community_scenario_view, community_scenario_delete, community_scenario_write, community_scenario_write_done, s_comment_write_done, community_scenario_download

urlpatterns = [
	url(r'^freeboard/list/$', freeboard_list, name='freeboard_list'),
	url(r'^freeboard/view/$', freeboard_view, name='freeboard_view'),
	url(r'^freeboard/write/$', freeboard_write, name='freeboard_write'),
	url(r'^freeboard/write/done/$', freeboard_write_done, name='freeboard_write_done'),
	url(r'^freeboard/comment/done/$', comment_write_done, name='f_comment_write_done'),
	url(r'^freeboard/delete/$', freeboard_delete, name='freeboard_delete'),

	url(r'^report/list/$', community_scenario_list, name='community_scenario_list'),
	url(r'^report/view/$', community_scenario_view, name='community_scenario_view'),
	url(r'^report/write/$', community_scenario_write, name='community_scenario_write'),
	url(r'^report/write/done/$', community_scenario_write_done, name='community_scenario_write_done'),
	url(r'^report/comment/done/$', s_comment_write_done, name='s_comment_write_done'),
	url(r'^report/delete/$', community_scenario_delete, name='community_scenario_delete'),
	url(r'^report/download/$', community_scenario_download, name='community_scenario_download'),
]
