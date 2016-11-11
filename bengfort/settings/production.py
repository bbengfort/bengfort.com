# bengfort.settings.production
# Settings for Bengfort.com in production.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:13:12 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: production.py [11b57d0] benjamin@bengfort.com $

"""
Settings for Bengfort.com in production.
"""

##########################################################################
## Imports
##########################################################################

import os
from .base import *


##########################################################################
## Production Settings
##########################################################################

## Debug must be false.
DEBUG = False

## Hosts
ALLOWED_HOSTS    = [
    'bengfort.herokuapp.com',
    'bengfort.com',
    'www.bengfort.com',
]

## Static files served by WhiteNoise
STATIC_ROOT = os.path.join(PROJECT, 'staticfiles')

##########################################################################
## Import Local Settings
##########################################################################

try:
    from .local import *
except ImportError:
    pass
