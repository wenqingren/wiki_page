# -*- coding: utf-8 -*-
import markdown

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render

from wikipage.forms import WikiPageForm
from wikipage.models import Page, PageLog
from wikipage.utils import get_shown_page_title


def wikipage_index(request):
    if request.method == 'GET' and 'wikipage_search' in request.GET and request.GET['wikipage_search']:
        wikipage_search = request.GET['wikipage_search']
        wikipage_list = Page.objects.filter(title__icontains=wikipage_search).order_by('title')
        if wikipage_list.count() == 1:
            return HttpResponseRedirect(reverse('wikipage_detail', args=[wikipage_list[0].title]))
        info = 'Searched Wiki Page Result:'
    else:
        wikipage_list = Page.objects.all().order_by('title')
        info = ''
    t = loader.get_template('wikipage/index.html')
    context_values = {
        'wikipage_list': wikipage_list,
        'info': info,
    }
    c = Context(context_values)
    return HttpResponse(t.render(c))


def wikipage_detail(request, wikipage_title):
    try:
        wikipage_obj = Page.objects.get(title=wikipage_title)
        shown_title = get_shown_page_title(wikipage_title)
    except Page.DoesNotExist:
        wikipage_obj = None
        shown_title = 'The page "%s" does not exist' %  get_shown_page_title(wikipage_title)

    t = loader.get_template('wikipage/wikipage_details.html')
    c = Context({
        'wikipage': wikipage_obj,
        'page_title': wikipage_title,
        'shown_title': shown_title,
        'page_body': markdown.markdown(wikipage_obj.get_current_contents().body) if wikipage_obj else ''
    })
    return HttpResponse(t.render(c))


def edit_wikipage(request, wikipage_title):
    try:
        edited_wikipage = Page.objects.get(title=wikipage_title)
    except Page.DoesNotExist:
        edited_wikipage = None
    if request.method == 'POST':
        form = WikiPageForm(request.POST or None)
        if form.is_valid():
            if not edited_wikipage:
                edited_wikipage = Page.objects.create(title=wikipage_title)
            edited_wikipage.create_new_log(body=form.cleaned_data['body'], comment=form.cleaned_data['comment'])

            response = HttpResponseRedirect(reverse('wikipage_detail', args=[wikipage_title]))
            return response
    else:
        if edited_wikipage:
            page_log = edited_wikipage.get_current_contents()
        else:
            page_log = None
        if page_log:
            form = WikiPageForm({'body': page_log.body, 'comment': ''})
        else:
            form = WikiPageForm()

    response = render(request, 'wikipage/edit_wikipage.html', {'form': form, 'wikipage_title': wikipage_title})
    return response


def wikipage_history(request, wikipage_title):
    wikipage = get_object_or_404(Page, title=wikipage_title)

    t = loader.get_template('wikipage/wikipage_history.html')
    c = Context({
        'wikipage_title': wikipage_title,
        'history_list': wikipage.get_history_list(),
    })
    return HttpResponse(t.render(c))


def global_history(request):
    t = loader.get_template('wikipage/global_history.html')
    c = Context({
        'history_list': PageLog.objects.order_by('-update_time', 'page'),
    })
    return HttpResponse(t.render(c))
