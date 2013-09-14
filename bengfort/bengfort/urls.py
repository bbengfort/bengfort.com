# bengfort.urls
# The main routes for the Bengfort application
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 16:40:47 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
The main routes for the Bengfort web application.
"""

##########################################################################
## Imports
##########################################################################

from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url

##########################################################################
## Routes
##########################################################################

admin.autodiscover()

urlpatterns = patterns('',
    # Temporary Index View
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    # Admin site
    url(r'grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
