# bengfort.templatetags.bengfort_tags
# Global tags for use across the Bengfort.com project
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 14:47:51 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: bengfort_tags.py [] benjamin@bengfort.com $

"""
Global tags for use across the Bengfort.com project
"""

##########################################################################
## Imports and Module Constants
##########################################################################

from django import template

# Create hook to template library
register = template.Library()


##########################################################################
## Assignment Tags
##########################################################################

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # Returns a core.Page, not implementation-specific model so object
    # comparison to self will return false as objects differ.
    return context['request'].site.root_page


##########################################################################
## Inclusion Tags
##########################################################################

@register.inclusion_tag('tags/navbar.html', takes_context=True)
def navbar(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for item in menuitems:
        item.active = (
            calling_page.url.startswith(item.url)
            if calling_page else False
        )

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }
