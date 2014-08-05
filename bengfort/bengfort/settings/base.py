# bengfort.settings.base
# The common Django settings for the Bengfort.com site
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Aug 04 23:02:25 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: base.py [] benjamin@bengfort.com $

"""
Django settings for bengfort project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

##########################################################################
## Imports
##########################################################################

import os
from django.conf import global_settings

##########################################################################
## Helper function for environmental settings
##########################################################################

def environ_setting(name, default=None):
    """
    Fetch setting from the environment- if not found, then this setting is
    ImproperlyConfigured.
    """
    if name not in os.environ and default is None:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(
            "The {0} ENVVAR is not set.".format(name)
        )

    return os.environ.get(name, default)

##########################################################################
## Build Paths inside of project with os.path.join
##########################################################################

BASE_DIR    = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.normpath(os.path.join(BASE_DIR, os.pardir))

##########################################################################
## Secret settings - do not store!
##########################################################################

## SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ_setting("SECRET_KEY")

##########################################################################
## Database Settings
##########################################################################

## See https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ_setting('DB_NAME', 'bengfort'),
        'USER': environ_setting('DB_USER', 'django'),
        'PASSWORD': environ_setting('DB_PASS', ''),
        'HOST': environ_setting('DB_HOST', 'localhost'),
        'PORT': environ_setting('DB_PORT', '5432'),
    },
}

##########################################################################
## Runtime settings
##########################################################################

## Debugging settings
## SECURITY WARNING: don't run with debug turned on in production!
DEBUG          = True
TEMPLATE_DEBUG = True

## Hosts
ALLOWED_HOSTS  = []
INTERNAL_IPS   = ('127.0.0.1', '198.168.1.10')

## WSGI Configuration
ROOT_URLCONF     = 'bengfort.urls'
WSGI_APPLICATION = 'bengfort.wsgi.application'

## Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## Third party apps
    'south',
    'compressor',
    'taggit',
    'modelcluster',
    'django.contrib.admin',

    ## Wagtail apps
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',

    ## Bengfort.com apps
    'scribe',
)

## Request Handling
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

## Internationalization
## https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'America/New_York'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

## Auth settings
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

##########################################################################
## Content (Static, Media, Templates)
##########################################################################

## Static files (CSS, JavaScript, Images)
## https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL          = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS    = (
    os.path.join(PROJECT_DIR, 'static'),
)

## Compressor Settings
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

## Template Files.
TEMPLATE_DIRS       = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

## Uploaded Media
MEDIA_URL           = "/media/"

##########################################################################
## Logging and Error Reporting
##########################################################################

ADMINS          = (
    ('Benjamin Bengfort', 'benjamin@bengfort.com'),
)

SERVER_EMAIL    = 'Dakota <server@bengfort.com>'
EMAIL_USE_TLS   = True
EMAIL_HOST      = 'smtp.gmail.com'
EMAIL_HOST_USER = 'server@bengfort.com'
EMAIL_HOST_PASSWORD  = environ_setting("EMAIL_HOST_PASSWORD")
EMAIL_PORT      = 587
EMAIL_SUBJECT_PREFIX = '[Bengfort.com]'

##########################################################################
## AWS Access Keys
##########################################################################

AWS_ACCESS_KEY_ID       = environ_setting('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY   = environ_setting('AWS_SECRET_KEY', '')
AWS_STORAGE_BUCKET_NAME = environ_setting('AWS_S3_BUCKET', 'bengfort')
AWS_QUERYSTRING_AUTH    = True
AWS_DEFAULT_ACL         = 'private'

##########################################################################
## Wagtail Settings
##########################################################################

WAGTAIL_SITE_NAME = 'Bengfort.com'

## Override the search results template for wagtailsearch
WAGTAILSEARCH_RESULTS_TEMPLATE = 'search_results.html'
