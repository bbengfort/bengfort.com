# spotlight.admin
# Register admin site details for Spotlight
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 18:49:50 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
User profile models for the Spotlight app.
"""

##########################################################################
## Imports
##########################################################################

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from spotlight.models import Profile, ProfileLink

##########################################################################
## Admin classes and Inlines
##########################################################################

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):

    inlines = (ProfileInline, )

##########################################################################
## Admin Registration
##########################################################################

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ProfileLink)
