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
