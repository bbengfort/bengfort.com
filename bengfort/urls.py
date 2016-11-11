# bengfort.urls
# Application URL definition and routers.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:50:02 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: urls.py [11b57d0] benjamin@bengfort.com $

"""
Application URL definition and routers.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/

Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

##########################################################################
## Imports
##########################################################################

from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.conf.urls import include, url

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from bengfort.views import *


##########################################################################
## Endpoint Discovery
##########################################################################

## API
router = routers.DefaultRouter()
router.register(r'status', HeartbeatViewSet, "status")


##########################################################################
## URL Patterns
##########################################################################

urlpatterns = [
    # The regular Django Admin
    url(r'^django-admin/', include(admin.site.urls)),

    # Wagtail CMS
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # Wagtail Search
    url(r'^search/$', search_views.search, name='search'),

    # REST API
    url(r'^api/', include(router.urls, namespace='api')),

    # CMS endpoints !important: must be last
    url(r'', include(wagtail_urls)),
]


##########################################################################
## Debugging URLs
##########################################################################

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
