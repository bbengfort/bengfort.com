# scribe.models
# Models for the basic scribe app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Tue Aug 05 14:39:07 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
Models for the basic scribe app
"""

##########################################################################
## Imports
##########################################################################

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import InlinePanel, PageChooserPanel

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

##########################################################################
## HomePage Model
##########################################################################

class HomePage(Page):

    ## Fields
    body = RichTextField(blank=True)

    ## Search
    indexed_fields = ('body', )

    ## Meta
    class Meta:
        verbose_name = "Homepage"

## Admin for the HomePage
HomePage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('body', classname='full'),
]

HomePage.promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
]
