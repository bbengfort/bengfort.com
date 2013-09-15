# spotlight.views
# Views for the Spotlight app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 21:12:21 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: views.py [] benjamin@bengfort.com $

"""
Views for the spotlight app.
"""

##########################################################################
## Imports
##########################################################################

from spotlight.models import Profile, Author
from django.views.generic import DetailView

##########################################################################
## Model Detail Views
##########################################################################

class ProfileView(DetailView):

    model = Author
    template_name = "profile.html"
    slug_field = 'username'
    slug_field_kwarg = 'username'
