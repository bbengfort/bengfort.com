# scribe.models
# Post and article models in Scribe app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Sep 16 21:28:04 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [] benjamin@bengfort.com $

"""
We're doing our own blog app... yep, that's right!
"""

##########################################################################
## Imports
##########################################################################

from django.db import models
from markdown import markdown
from django.utils import timezone
from django.utils.html import strip_tags
from django.template.defaultfilters import slugify
from scribe.managers import DRAFT, HIDDEN, PUBLISHED
from django.utils.translation import ugettext_lazy as _

##########################################################################
## Models
##########################################################################

class Entry(models.Model):
    """
    The base model for a blog post or an article.

    Todo: Implement more than just markdown writing
    Todo: Implement tagging of some sort
    Todo: Implement sites
    Todo: Implement discussions (comments)
    Todo: Implement related entries
    """

    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (HIDDEN, _('hidden')),
        (PUBLISHED, _('published')),
    )

    title      = models.CharField(_('title'), max_length=255)
    slug       = models.SlugField(_('slug'), max_length=255, unique_for_date='created', blank=True)
    status     = models.SmallIntegerField(_('status'), choices=STATUS_CHOICES, default=DRAFT)
    created    = models.DateTimeField(_('created on'), default=timezone.now)
    updated    = models.DateTimeField(_('last updated'), default=timezone.now)
    pubdate    = models.DateTimeField(_('publish on'), default=timezone.now)
    content    = models.TextField(_('content'), blank=True)
    excerpt    = models.TextField(_('excerpt'), blank=True)
    image      = models.ImageField(_('image'), null=True, blank=True, upload_to='uploads/%Y/%m')
    featured   = models.BooleanField(_('featured'), default=False)
    author     = models.ForeignKey('spotlight.Author', related_name='entries')
    categories = models.ManyToManyField('scribe.Category', related_name='entries')

    @property
    def word_count(self):
        """
        Counts the number of words in the content.
        """
        return len(strip_tags(self.to_html()).split())

    def is_visible(self):
        """
        Checks if an entry is visible and published
        """
        return self.pubdate < timezone.now() and self.status == PUBLISHED

    def to_html(self):
        """
        Renders the markdown content in HTML
        """
        return markdown(self.content)

    @models.permalink
    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on the slug.
        """
        published = self.pubdate
        if timezone.is_aware(published):
            published = timezone.localtime(published)
        return ('scribe_entry_detail', (), {
                'year': published.strftime('%Y'),
                'month': published.strftime('%m'),
                'day': published.strftime('%d'),
                'slug': self.slug
            })

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return '%s: %s' % (self.tile, self.get_status_display())

    def __len__(self):
        return self.word_count

    class Meta:
        ordering = ['-pubdate']
        get_latest_by = 'pubdate'
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        index_together = [['slug', 'pubdate']]

class Category(models.Model):
    """
    The base model for implementing categories

    Todo: Use MPTT
    """

    title  = models.CharField(_('title'), max_length=255)
    slug   = models.CharField(_('slug'), max_length=255)
    notes  = models.TextField(_('notes'), blank=True, null=True, default=None)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    @property
    def tree_path(self):
        """
        Returns category's tree path by concatening the slug of his
        ancestors.
        """
        ancestors = []
        parent = self
        while parent:
            ancestors.append(parent.slug)
            parent = parent.parent
        ancestors.reverse()
        return '/'.join(ancestors)

    @models.permalink
    def get_absolute_url(self):
        return ('scribe_category_detail', (self.tree_path,))

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _('category')
        verbose_name_plural = _('categories')
