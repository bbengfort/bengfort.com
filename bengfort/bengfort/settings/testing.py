# bengfort.settings.testing
# The Django settings for the Bengfort.com site in Testing
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Aug 04 23:12:23 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: testing.py [] benjamin@bengfort.com $

"""
The Django settings for the Bengfort.com site in Testing
"""

##########################################################################
## Imports
##########################################################################
#
import os
from .base import *

##########################################################################
## Testing Settings
##########################################################################

## Debugging Settings
DEBUG            = True
TEMPLATE_DEBUG   = True

## Hosts
ALLOWED_HOSTS    = ['localhost', '127.0.0.1']

## Database Settings
DATABASES = {
    'default': {
        'PASSWORD': 'tr4v1sT3ST3R!',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
