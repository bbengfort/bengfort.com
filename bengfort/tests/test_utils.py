# bengfort.tests.test_utils
# Test the project level utilities and helper functions.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 10:32:03 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: test_utils.py [] benjamin@bengfort.com $

"""
Test the project level utilities and helper functions.
"""

##########################################################################
## Imports
##########################################################################

import unittest

from bengfort.utils import *


##########################################################################
## Utilities Tests
##########################################################################

class UtilitiesTests(unittest.TestCase):

    def test_normalize(self):
        """
        Test the normalize helper function
        """

        cases = (
            ('The big bad BEAR', 'thebigbadbear'),
            ('#GOING#HOME', 'goinghome'),
            ('This is the best!', 'thisisthebest'),
            ('#!#!%#!@^!#$^#$%%&$%&()&()_)()<>,.?/', ''),
        )

        for case, expected in cases:
            self.assertEqual(normalize(case), expected)

    def test_signature(self):
        """
        Test the SHA1 signature function
        """

        cases = (
            ('The eagle flies at midnight', 'tEkJqBDX2i4eQnQztBPDMLMTUSqcqvbWdadTvWfnjVg='),
            ('bandsawtruck', 'IDLW3A5AVLftGb/kNtKxv/wXk8szwUDSU8ejSPeMTTM='),
        )

        for case, expected in cases:
            self.assertEqual(signature(case), expected)


if __name__ == '__main__':
    unittest.main()
