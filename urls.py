# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wikipage.views.wikipage_index'),
    url(r'^wiki/(?P<wikipage_title>[0-9A-Za-z/_-]+)/$', 'wikipage.views.wikipage_detail', name='wikipage_detail'),
    url(r'^wikipage/', include("wikipage.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
