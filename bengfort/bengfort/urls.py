# bengfort.urls
# Main controller for the Bengfort.com application
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Aug 04 23:51:14 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [] benjamin@bengfort.com $

"""
Main controller for the Bengfort.com application
"""

##########################################################################
## Imports
##########################################################################

## Configuration
from django.conf import settings

## Django Imports
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

## Wagtail Imports
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch.urls import frontend as wagtailsearch_frontend_urls
from wagtail.wagtailsearch import register_signal_handlers as wagtailsearch_register_signal_handlers

##########################################################################
## Signals and Autoconfiguration
##########################################################################

## Django Admin discovery
admin.autodiscover()

## Register signal handlers
wagtailsearch_register_signal_handlers()

##########################################################################
## URL Patterns
##########################################################################

urlpatterns = patterns('',
    ## Django Admin
    url(r'^django-admin/', include(admin.site.urls)),

    ## CMS URLs
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_frontend_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
)

##########################################################################
## Development Handler
##########################################################################

if settings.DEBUG:
    import os
    from django.conf.urls.static import static
    from django.views.generic.base import RedirectView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += patterns('',
        (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'demo/images/favicon.ico'))
    )
