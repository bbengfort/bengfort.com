# bengfort.settings.production
# The Django settings for the Bengfort.com site in Production
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Aug 04 23:02:30 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: production.py [] benjamin@bengfort.com $

"""
The Django settings for the Bengfort.com site in Production
"""

##########################################################################
## Imports
##########################################################################

import os
from .base import *

##########################################################################
## Production Settings
##########################################################################

## Debugging Settings
DEBUG            = False
TEMPLATE_DEBUG   = False

## Hosts
ALLOWED_HOSTS    = ['bengfort.com',
                    'localhost', '127.0.0.1']

## Static files served by Nginx
STATIC_ROOT = '/var/www/stacks/static'
MEDIA_ROOT  = '/var/www/stacks/media'

## Application Environment
INSTALLED_APPS+= (
    'djcelery',
    'kombu.transport.django',
    'gunicorn',
)

##########################################################################
## Cache Settings
##########################################################################

## Template Loaders
## Use the cached template loader
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'KEY_PREFIX': 'bengfort',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

## CELERY SETTINGS
import djcelery
djcelery.setup_loader()

BROKER_URL = 'redis://'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False

##########################################################################
## Search Settings
##########################################################################

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'wagtaildemo'
    }
}
