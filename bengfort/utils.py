# bengfort.utils
# Project level utilities and helper functions.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Nov 11 10:29:54 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: utils.py [8fcbaab] benjamin@bengfort.com $

"""
Project level utilities and helper functions.
"""

##########################################################################
## Imports
##########################################################################

import re
import base64
import hashlib


##########################################################################
## Utilities
##########################################################################

## Nullable kwargs for models
nullable = { 'blank': True, 'null': True, 'default':None }

## Not nullable kwargs for models
notnullable = { 'blank': False, 'null': False }


##########################################################################
## Helper functions
##########################################################################

def normalize(text):
    """
    Normalizes the text by removing all punctuation and spaces as well as
    making the string completely lowercase.
    """
    return re.sub(r'[^a-z0-9]+', '', text.lower())


def signature(text):
    """
    This helper method normalizes text and takes the SHA1 hash of it,
    returning the base64 encoded result. The normalization method includes
    the removal of punctuation and white space as well as making the case
    completely lowercase. These signatures will help us discover textual
    similarities between questions.
    """
    text = normalize(text).encode('utf-8')
    sign = base64.b64encode(hashlib.sha256(text).digest())
    return sign.decode('utf-8')
