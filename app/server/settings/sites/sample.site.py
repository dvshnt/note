import os
from server.settings.base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ' -- NAME OF DB --',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': ' -- DB USER -- ',
        'PASSWORD': ' -- DB PASSWORD -- ',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'


STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'


STATICFILES_DIRS = (' -- PATH TO STATIC FILES DIR -- ',)


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ' -- PATH TO TEMPLATE DIR -- ',
    #os.path.join(BASE_DIR, 'client', 'views')
)


# Admins for bug reports
ADMINS = ( 
    (' NAME OF ADMIN ', 'EMAIL OF ADMIN'),
)


MANAGERS = ADMINS


SITE_ID = 2


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bg_tg!$q)=7^x*9fr2+gfz9$=z=$#l5yxnu2_xt(lun+i=ne&t'


ROOT_URLCONF = 'server.urls'


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'path.to.wsgi.application'