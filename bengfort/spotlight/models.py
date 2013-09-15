# spotlight.models
# User profile models in Spotlight app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 18:49:20 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
User profile models for the Spotlight pap.
"""

##########################################################################
## Imports
##########################################################################

import urllib
import hashlib

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

##########################################################################
## Models
##########################################################################

class Profile(models.Model):

    user      = models.OneToOneField('auth.User', editable=False, related_name='profile')
    biography = models.TextField( blank=True, null=True, default=None )
    shortbio  = models.CharField( max_length=156, blank=True, null=True, default=None)

    @property
    def gravatar(self):
        size    = 120
        default = "mm"
        digest  = hashlib.md5(self.user.email.lowe()).hexdigest()
        params  = urllib.urlencode({'d': default, 's': str(size)})
        gravurl = "http://www.gravatar.com/avatar/%s?%s" % (digest, params)
        return gravurl

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def full_email(self):
        email = "%s <%s>" % (self.full_name, self.user.email)
        return email.strip()

    def delete(self, using=None):
        self.user.delete(using=using)
        super(Profile, self).delete(using=using)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

class ProfileLink(models.Model):

    SOCIAL_LINK_TYPES = (
        ("BL", "Blogger"),
        ("D", "Delicious"),
        ("DG", "Digg"),
        ("Dr", "Dribble"),
        ("FB", "Facebook"),
        ("FL", "Flickr"),
        ("FR", "Forrst"),
        ("GH", "Github"),
        ("G", "Google"),
        ("IG", "Instagram"),
        ("LI", "LinkedIn"),
        ("P", "Pinterest"),
        ("R", "Reddit"),
        ("RS", "RSS"),
        ("ST", "ShareThis"),
        ("Sy", "Skype"),
        ("SU", "Stumble Upon"),
        ("TR", "Tumblr"),
        ("TW", "Twitter"),
        ("V", "Vimeo"),
        ("WP", "Wordpress"),
        ("YT", "YouTube"),
        ("O", "Other"),
    )

    profile = models.ForeignKey( Profile, related_name='links' )
    href    = models.URLField( verbose_name='URL' )
    target  = models.CharField( max_length=2, choices=SOCIAL_LINK_TYPES )

    @classmethod
    def type_from_name(klass, name):
        name = name.lower()
        if name not in klass._name_link_map:
            raise KeyError("'%s' is not in the SOCIAL_LINK_TYPES enumeration" % name)
        return klass._name_link_map[name]

    def get_css_class(self):
        target = self.get_target_display().lower().replace(" ", "-")
        return target

    def get_css_title(self):
        return self.get_target_display()

    def __unicode__(self):
        return self.href

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
        unique_together = (("profile", "target"),)

##########################################################################
## Proxy Object for Users
##########################################################################

class Author(User):
    """
    Proxy class for django.contrib.auth.models.User for enacting our
    methods and management on the User database without affecting the
    User class.
    """

    @classmethod
    def fromUser(klass, user):
        return klass.objects.get(pk=user.pk)

    @property
    def gravatar(self):
        size    = 120
        default = "mm"
        digest  = hashlib.md5(self.email.lower()).hexdigest()
        params  = urllib.urlencode({'d':default, 's':str(size)})
        gravurl = "http://www.gravatar.com/avatar/%s?%s" % (digest, params)
        return gravurl

    @property
    def full_name(self):
        return self.get_full_name()

    @property
    def full_email(self):
        return self.get_profile().full_email

    def get_author(self):
        return Author.objects.get(pk=self.pk)

    class Meta:
        proxy= True
