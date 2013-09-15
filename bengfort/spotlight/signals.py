# spotlight.signals
# Singals in Spotlight app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 19:11:56 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: signals.py [] benjamin@bengfort.com $

"""
Singals for the Spotlight app.
"""

##########################################################################
## Imports
##########################################################################

from django.db.models import signals
from spotlight.models import Profile, Author
from django.contrib.auth.models import User

##########################################################################
## Signals Methods
##########################################################################

def create_profile(sender, instance, signal, created, **kwargs):
    """
    When a user is created, also create a matching profile.
    If raw is set, this is being loaded from a fixture, so ignore.
    """
    if created and not kwargs.get('raw', False):
        Profile(user=instance).save()

##########################################################################
## Register signals
##########################################################################

signals.post_save.connect(create_profile, sender=User)
signals.post_save.connect(create_profile, sender=Author)
