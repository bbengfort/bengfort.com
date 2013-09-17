# scribe.tests
# Tests for the Scribe app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Sep 16 22:26:47 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: tests.py [] benjamin@bengfort.com $

"""
Test the Scribe app's views, signals, and models
"""

from django.test import TestCase
from django.contrib.auth.models import User
from scribe.models import Entry, Category
from spotlight.models import Author

class ScribeEntryModelTest(TestCase):

    fixtures = ['authors.json']

    def setUp(self):
        self.author = Author.objects.get(username='benjamin')

    def test_slugify(self):
        """
        Ensure that slugify is run on save
        """
        e = Entry(title="Test", author=self.author)
        e.save()
        self.assertTrue(e.slug)

    def test_slugify_create(self):
        """
        Ensure that slugify is run on save
        """
        e = Entry.objects.create(title="Test", author=self.author)
        self.assertTrue(e.slug)

    def test_word_count(self):
        """
        Assert that the wordcount mechanism works.
        """

        content = ("This is a very simple entry that has a number of "
                   "words in it, and it is a very good thing to do.\n\n"
                   "In markdown, this should be the second paragraph.")
        e = Entry(title="Test", author=self.author, content=content)
        e.save()

        self.assertEqual(e.word_count, 31)

class ScribeCategoryModelTest(TestCase):

    def test_slugify_save(self):
        """
        Ensure that slugify is run on save
        """
        c = Category(title="Test")
        c.save()
        self.assertTrue(c.slug)

    def test_slugify_create(self):
        """
        Ensure that slugify is run on save
        """
        c = Category.objects.create(title="Test")
        self.assertTrue(c.slug)

    def test_tree_path(self):
        """
        Check the treepath building mechanism
        """

        root = Category.objects.create(title='General')
        next = Category.objects.create(title='Software Development', parent=root)
        more = Category.objects.create(title='Python', parent=next)
        last = Category.objects.create(title='Django', parent=more)

        self.assertEqual(last.tree_path, 'general/software-development/python/django')
