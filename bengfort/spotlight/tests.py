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

class SpotlightTest(TestCase):

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
