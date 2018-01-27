from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-bwr19^)+1hqj3j9nmtc_i*_jer4%+%foscnhbhvlg6h0ycgj)'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS = [
    'home',
    'search',
    'blog',
    'base',
    'tours',

    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.modeladmin',

    'modelcluster',
    'taggit',

    'wagtailmenus',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
