from django import template

register = template.Library()

@register.filter(name='scenario_problem_num')
def scenario_problem_num(value):
	return value % 100
