# scribe.managers
# Post and article managers in Scribe app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Sep 16 21:33:26 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: managers.py [] benjamin@bengfort.com $

"""
Managers for the entry model.
"""

##########################################################################
## Imports
##########################################################################

from django.db import models

##########################################################################
## CVARs
##########################################################################

DRAFT     = 0
HIDDEN    = 1
PUBLISHED = 2

##########################################################################
## Managers
##########################################################################
