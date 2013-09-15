# spotlight.urls
# Routes for the Spotlight app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 21:10:23 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
Subroutes for the spotlight app.

Note: routes expect a username argument from the main routes.
"""

##########################################################################
## Imports
##########################################################################

from spotlight.views import *
from django.conf.urls import patterns, include, url

##########################################################################
## Routes
##########################################################################

urlpatterns = patterns('',
    url(r'^$', ProfileView.as_view()),
)
