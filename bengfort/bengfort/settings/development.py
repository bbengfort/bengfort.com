# bengfort.settings.development
# The Django settings for the Bengfort.com site in Development
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Aug 04 23:01:24 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: development.py [] benjamin@bengfort.com $

"""
The Django settings for the Bengfort.com site in Development
"""

##########################################################################
## Imports
##########################################################################

import os
from .base import *

##########################################################################
## Development Settings
##########################################################################

## Debugging Settings
DEBUG            = True
TEMPLATE_DEBUG   = True

## Hosts
ALLOWED_HOSTS    = ('127.0.0.1', 'localhost')

## Secret Key doesn't matter in Dev
SECRET_KEY = 'cyt*c1@%sg6j@g6y9fdrd@iakg7)ek!dqb@7grl(c-nkm%2596'

## Content
MEDIA_ROOT       = os.path.join(PROJECT_DIR, 'media')
