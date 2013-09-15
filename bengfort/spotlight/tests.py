# spotlight.tests
# Tests for the Spotlight app
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 14 20:15:44 2013 -0400
#
# Copyright (C) 2013 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: tests.py [] benjamin@bengfort.com $

"""
Test the Spotlight app's views, signals, and models
"""

from django.test import TestCase
from django.contrib.auth.models import User
from spotlight.models import Profile, Author

class SpotlightModelTest(TestCase):

    def test_user_post_save_profile(self):
        """
        Ensure a profile is created on User save.
        """

        # Create a user
        user = User.objects.create_user('test', 'test@example.com', 's3cr3t')

        # Assert that a profile exists for the user
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_proxy_post_save_profile(self):
        """
        Ensure a profile is created on User Proxy save.
        """
        # Create an Author
        user = Author.objects.create_user('test', 'test@example.com', 's3cr3t')

        # Assert that a profile exists for the user
        self.assertTrue(Profile.objects.filter(user=user).exists())

class SpotlightViewTest(TestCase):

    fixtures = ['benjamin.json', 'users.json']

    def test_profile_get(self):
        """
        Assert a profile is viewable if it exists in DB
        """
        resp = self.client.get('/benjamin/')
        self.assertEqual(resp.status_code, 200)

    def test_profile_context(self):
        """
        Assert context is delivering an object
        """
        resp = self.client.get('/benjamin/')
        self.assertIn('object', resp.context)

    def test_profile_instance(self):
        """
        Assert a context is delivering an Author
        """
        resp = self.client.get('/benjamin/')
        self.assertTrue(isinstance(resp.context['object'], Author))
