# blog.models
# Models for our blog pages
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 11:58:42 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: models.py [741ab42] benjamin@bengfort.com $

"""
Models for our blog pages
"""

##########################################################################
## Imports
##########################################################################

from django.db import models
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager

from wagtail.wagtailsearch import index
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel


##########################################################################
## Index and Listing Pages
##########################################################################

class BlogIndex(Page):
    """
    A paginated list of all published blog posts in reverse chronological
    order. There should be only one blog index page (usually).
    """

    # Database fields
    intro = RichTextField(blank=True, help_text='brief content before listing')

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

     # Parent page / subpage type rules
    subpage_types = ['blog.BlogPost']


    def get_blog_posts(self):
        """
        Returns a queryset of blog posts associated with the index.
        """
        return self.get_children().live().order_by('-first_published_at')

    def get_context(self, request):
        """
        Update the context to include the blog posts in the index.
        """
        context = super(BlogIndex, self).get_context(request)
        posts = self.get_blog_posts()

        # Pagination
        page = request.GET.get('page')
        page_size = 1
        if hasattr(settings, 'BLOG_PAGINATION_PER_PAGE'):
            page_size = settings.BLOG_PAGINATION_PER_PAGE

        if page_size is not None:
            paginator = Paginator(posts, page_size)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        return context


class BlogTagIndex(Page):
    """
    A paginated list of published blog posts associated with a particular tag.
    """

    def get_posts_by_tag(self, tag):
        """
        Returns a queryset of blog posts associated with the given tag.
        """
        return BlogPost.objects.filter(tags__name=tag)

    def get_context(self, request):
        """
        Use the GET query string to return posts based on the tag.
        """
        context = super(BlogTagIndex, self).get_context(request)

        # Filter blog posts by tag
        tag = request.GET.get('tag')
        context["posts"] = self.get_posts_by_tag(tag)

        return context


##########################################################################
## Blog Posts
##########################################################################

class BlogPostTag(TaggedItemBase):
    """
    Connects a Blog Post with tags
    """

    # Database fields
    content_object = ParentalKey('blog.BlogPost', related_name='tagged_items')


class BlogPostRelatedLink(Orderable):
    """
    Connects a Blog Post with related links
    """

    # Database fields
    page = ParentalKey('blog.BlogPost', related_name='related_links')
    name = models.CharField(max_length=255, help_text='The title of the link')
    url  = models.URLField(help_text='The full URL of the link')

    # Editor panels configuration
    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]


class BlogPost(Page):
    """
    A blog post or article.
    """

    # Database fields
    date    = models.DateField("Post date", help_text='Displayed publication date.')
    excerpt = models.TextField(blank=True, help_text='A small excerpt describing the post.')
    body    = RichTextField(blank=True, help_text='The body of the blog post')
    tags    = ClusterTaggableManager(through='blog.BlogPostTag', blank=True)
    views   = models.IntegerField(default=0, blank=True, editable=False)
    author  = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True,
        verbose_name='Author', on_delete=models.SET_NULL,
        related_name='author_pages',
    )
    image   = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
        help_text='The featured image associated with the post',
    )

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('excerpt'),
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('author'),
        ], heading='Blog information'),
        FieldPanel('body', classname='full'),
        InlinePanel('related_links', label="Related links"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('excerpt', classname='full'),
        ImageChooserPanel('image'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['blog.BlogIndex']
    subpage_types = []

    def serve(self, request):
        """
        Override the serve method to implement page tracking.
        """

        # Check if the view marker is in the user session
        viewkey = "viewed_blog_post_{}".format(self.id)
        if not request.session.get(viewkey, False):

            # Increment the views and save
            self.views += 1
            self.save()

            # Add the view key to the session
            request.session[viewkey] = True

        return super(BlogPost, self).serve(request)

    def save_revision(self, *args, **kwargs):
        """
        Make sure that the author is saved with the revision.
        """
        if not self.author:
            self.author = self.owner
        return super(BlogPost, self).save_revision(*args, **kwargs)
