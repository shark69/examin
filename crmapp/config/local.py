
# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .settings import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
#DEBUG = env.bool('DJANGO_DEBUG', default=True)
#TEMPLATES[0]['OPTIONS']['debug'] = DEBUG



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dwexa',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
