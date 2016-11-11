# bengfort.tests.test_init
# Initialization tests for the Bengfort.com project.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 10:26:30 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: test_init.py [8fcbaab] benjamin@bengfort.com $

"""
Initialization tests for the Bengfort.com project.
"""

##########################################################################
## Imports
##########################################################################

from unittest import TestCase

##########################################################################
## Module variables
##########################################################################

EXPECTED_VERSION = "0.2"

##########################################################################
## Initialization Tests
##########################################################################

class InitializationTests(TestCase):
    """
    Some basic partisan tests
    """

    def test_sanity(self):
        """
        Check that the world is sane and 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Ensure the bengfort module can be imported
        """
        try:
            import bengfort
        except ImportError:
            self.fail("Could not import the bengfort module.")

    def test_version(self):
        """
        Assert that test and package versions match
        """
        import bengfort
        self.assertEqual(EXPECTED_VERSION, bengfort.__version__)
