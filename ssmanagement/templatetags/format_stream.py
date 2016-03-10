from __future__ import division
from django import template

register = template.Library()

@register.filter(name='streamformat')
def format_stream(value):
    value = long(value)
    if value < 1024:
        return '%sB' % value
    elif value < 1024*1024:
        return '%sK' % (value//1024)
    elif value < 1024*1024*1024:
        return '%.2fM' % (value/1024/1024)
    else:
        return '%.3fG' % (value/1024/1024/1024)
