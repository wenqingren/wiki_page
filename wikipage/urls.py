# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'wikipage.views.wikipage_index', name='wikipage_list'),
    url(r'^edit_wikipage/(?P<wikipage_title>[0-9A-Za-z/_-]+)/$', 'wikipage.views.edit_wikipage', name='edit_wikipage'),
    url(r'^wikipage_history/(?P<wikipage_title>[0-9A-Za-z/_-]+)/$', 'wikipage.views.wikipage_history', name='wikipage_history'),
    url(r'^global_history/$', 'wikipage.views.global_history', name='global_history'),
)
