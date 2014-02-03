# -*- coding: utf-8 -*-
import re


def get_shown_page_title(page_url):
    shown_title = re.sub('(.)([A-Z][a-z0-9]+)', r'\1 \2', page_url)
    shown_title = re.sub('([a-z0-9])([A-Z])', r'\1 \2', shown_title).title()
    shown_title = shown_title.replace('_', ' ').replace('/', ' / ')
    return ' '.join(shown_title.split())
