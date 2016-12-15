from django.contrib import admin

# Register your models here.

from .models import Notice
from .models import Freeboard, Comment_c
from .models import Community_scenario, Comment_scenario

class NoticeAdmin(admin.ModelAdmin):
	list_display = ('num', 'title', 'created_date')

class FreeboardAdmin(admin.ModelAdmin):
	list_display = ('num', 'title', 'author', 'created_date')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('num', 'freeboard', 'author', 'created_date')

class Community_scenarioAdmin(admin.ModelAdmin):
	list_display = ('num', 'title', 'author', 'created_date')

class Comment_scenarioAdmin(admin.ModelAdmin):
	list_display = ('num', 'c_scenario', 'author', 'created_date')

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Freeboard, FreeboardAdmin)
admin.site.register(Comment_c, CommentAdmin)
admin.site.register(Community_scenario, Community_scenarioAdmin)
admin.site.register(Comment_scenario, Comment_scenarioAdmin)
