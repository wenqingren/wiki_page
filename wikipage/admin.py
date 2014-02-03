# -*- coding: utf-8 -*-
from django.contrib import admin

from wikipage.models import Page, PageLog


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ['title']


class PageLogAdmin(admin.ModelAdmin):
    list_display = ('page', 'body', 'comment', 'update_time', 'is_current')
    search_fields = ['page', 'body', 'comment']


admin.site.register(Page, PageAdmin)
admin.site.register(PageLog, PageLogAdmin)
