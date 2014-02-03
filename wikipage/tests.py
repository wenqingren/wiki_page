# -*- coding: utf-8 -*-
"""
Unit Test to wikipage application
"""
from django.test import TestCase

from wikipage.models import Page
from wikipage.utils import get_shown_page_title


class TestShownPageTitle(TestCase):
    def test_resolve_wikipage_title(self):
        # test to make sure the resolve the page url to shown title is correct
        page_title = get_shown_page_title(u'human_body')
        self.assertEquals(page_title, 'Human Body')

        page_title = get_shown_page_title(u'HumanBody')
        self.assertEquals(page_title, 'Human Body')

        page_title = get_shown_page_title(u'Parts_of-the_HumanBody')
        self.assertEquals(page_title, 'Parts Of-The Human Body')

        page_title = get_shown_page_title(u'HumanBody/Parts')
        self.assertEquals(page_title, 'Human Body / Parts')

        page_title = get_shown_page_title(u'testPage')
        self.assertEquals(page_title, 'Test Page')

        page_title = get_shown_page_title(u'test')
        self.assertEquals(page_title, 'Test')


class WikiPageTest(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title='TestPage')
        self.page.create_new_log(body='test body1', comment='comment it 1')
        self.page.create_new_log(body='test body2', comment='comment it 2')

    def test_wikipage(self):
        # make sure the methods of Page model are correct
        self.assertEquals(self.page.get_current_contents().body, 'test body2')
        self.assertEquals(self.page.get_current_contents().comment, 'comment it 2')
        self.assertEquals(self.page.get_history_list().count(), 2)
        self.assertEquals(self.page.get_history_list()[0].body, 'test body2')
        self.assertTrue(self.page.get_history_list()[0].is_current)
        self.assertFalse(self.page.get_history_list()[1].is_current)
