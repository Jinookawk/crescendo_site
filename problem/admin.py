from django.contrib import admin

# Register your models here.

from problem.models import Problem
from problem.models import Answerlog
from problem.models import Scenario

class ProblemAdmin(admin.ModelAdmin):
	list_display = ('num', 'title', 'created_date', 'level', 'artifact')

class AnswerlogAdmin(admin.ModelAdmin):
	list_display = ('num', 'problem_num', 'problem_title', 'submit_answer', 'submitter', 'submit_date')

class ScenarioAdmin(admin.ModelAdmin):
	list_display = ('snum', 'answer_num')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Answerlog, AnswerlogAdmin)
admin.site.register(Scenario, ScenarioAdmin)
