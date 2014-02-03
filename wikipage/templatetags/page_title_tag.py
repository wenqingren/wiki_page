# -*- coding: utf-8 -*-
from django import template

from wikipage.utils import get_shown_page_title

register = template.Library()


@register.filter
def shownpagetitle(value):
    if not value:
        return ''
    return get_shown_page_title(value)
