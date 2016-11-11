# bengfort.settings.testing
# Testing settings to enable testing on Travis with Django tests.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:14:42 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: testing.py [11b57d0] benjamin@bengfort.com $

"""
Testing settings to enable testing on Travis with Django tests.
"""

##########################################################################
## Imports
##########################################################################

import os
from .base import *

##########################################################################
## Test Settings
##########################################################################

## Debugging Settings
DEBUG            = True

## Hosts
ALLOWED_HOSTS    = ['localhost', '127.0.0.1']

## Database Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ_setting('DB_NAME', 'partisan'),
        'USER': environ_setting('DB_USER', 'postgres'),
        'PASSWORD': environ_setting('DB_PASS', ''),
        'HOST': environ_setting('DB_HOST', 'localhost'),
        'PORT': environ_setting('DB_PORT', '5432'),
    },
}

STATICFILES_STORAGE =  'django.contrib.staticfiles.storage.StaticFilesStorage'

## Content without? side effects
MEDIA_ROOT         = "/tmp/partisan-discourse/media"
STATIC_ROOT        = "/tmp/partisan-discourse/static"

##########################################################################
## Django REST Framework
##########################################################################

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
)
