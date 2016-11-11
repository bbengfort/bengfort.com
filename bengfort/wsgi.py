# bengfort.wsgi
# WSGI Config for the Bengfort.com website
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:20:19 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: wsgi.py [11b57d0] benjamin@bengfort.com $

"""
WSGI Config for the Bengfort.com website

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

##########################################################################
## Imports
##########################################################################

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


##########################################################################
## Configuration
##########################################################################

## Load settings from environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bengfort.settings.production")

## Create Whitenoise application
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
