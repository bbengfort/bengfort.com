# home.models
# Model description of the default Wagtail home app.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 11:15:02 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
Model description of the default Wagtail home app.
"""

##########################################################################
## Imports
##########################################################################

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


##########################################################################
## Home Page Model
##########################################################################

class HomePage(Page):

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]
