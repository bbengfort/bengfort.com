# bengfort.settings.development
# Django settings for Bengfort.com in development
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:11:23 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: development.py [11b57d0] benjamin@bengfort.com $

"""
Django settings for Bengfort.com in development
"""

##########################################################################
## Imports
##########################################################################

import os
from .base import *

##########################################################################
## Development Settings
##########################################################################

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG            = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY       = '^ad*=iup@21bcx8u9m-6j=#!fw49t^+grll*he-uh)f#e6_y%^'

# Print email out to the console
EMAIL_BACKEND    = 'django.core.mail.backends.console.EmailBackend'

## Hosts
ALLOWED_HOSTS    = ('127.0.0.1', 'localhost')

## Content
MEDIA_ROOT       = os.path.join(PROJECT, 'media')
STATIC_ROOT      = 'staticfiles'


##########################################################################
## Import Local Settings
##########################################################################

try:
    from .local import *
except ImportError:
    pass
