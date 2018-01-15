from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.53.31", "qizl.es", "localhost", "cms.qizl.es", "52.59.215.159"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-bwr19^)+1hqj3j9nmtc_i*_jer4%+%foscnhbhvlg6h0ycgj)'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
