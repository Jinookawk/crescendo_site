from django import template
from ..models import Notice

register = template.Library()

@register.inclusion_tag('_notice_history.html')
def notice_history():
	notices = Notice.objects.order_by('-num')[:3]
	size = len(notices)
	return {'notices': notices, 'size': size}
