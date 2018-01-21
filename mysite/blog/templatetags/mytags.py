import datetime
from django import template
from wagtail.wagtailcore.models import Page
from ..models import *

register = template.Library()


# Advert snippets
@register.inclusion_tag('tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'categories': BlogCategory.objects.all(),
        'request': context['request'],
    }


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
