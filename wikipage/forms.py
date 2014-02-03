# -*- coding: utf-8 -*-

from django import forms


class WikiPageForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea,
        label=u'Page Body')
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label=u'Edit Comment')
