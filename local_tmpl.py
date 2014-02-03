#-*- coding: utf-8 -*-
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'wikipage.db'),
    }
}
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates/static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

