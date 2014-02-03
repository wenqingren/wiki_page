# -*- coding: utf-8 -*-
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_current_contents(self):
        '''
        Get the current log info of the page
        '''
        try:
            return self.pagelog_set.filter(is_current=True)[0]
        except IndexError:
            return None

    def get_history_list(self):
        '''
        Get the change log of the page
        '''
        return self.pagelog_set.order_by('-is_current', '-update_time')

    def create_new_log(self, body, comment):
        '''
        create new log info of the page
        '''
        self.pagelog_set.update(is_current=False)
        return self.pagelog_set.create(body=body, comment=comment, is_current=True)


class PageLog(models.Model):
    page = models.ForeignKey(Page)
    body = models.TextField()
    comment = models.TextField(null=True, blank=True)
    update_time = models.DateTimeField(auto_now_add=True)
    is_current = models.BooleanField(default=False)

    def __unicode__(self):
        return u'Body: %s Comment: %s' % (self.body, self.comment)
