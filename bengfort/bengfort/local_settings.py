# bengfort.local_settings
# Django settings for Apollo, in development.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 16:42:02 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: local_settings.py [] benjamin@bengfort.com $

"""
Apollo specific settings for the project.
"""

##########################################################################
## Settings
##########################################################################

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bengfort',
        'USER': 'django',
        'PASSWORD': '$b34rfamilyR1VER$',
        'HOST': 'localhost',
        'PORT': '',
        'TEST_NAME': 'bengfort_testing',
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = '56ggzdj27SExK0bmNIq59uE3taKjhLuaOu1Gkh7FNoaj2Ak@ks'
