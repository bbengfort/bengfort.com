# version
# Helper module for managing versioning information.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Nov 10 16:18:47 2016 -0500
#
# Copyright (C) 2016 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: version.py [11b57d0] benjamin@bengfort.com $

"""
Helper module for managing versioning information.
"""

##########################################################################
## Versioning
##########################################################################

__version_info__ = {
    'major': 0,
    'minor': 3,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 0,
}


def get_version(short=False):
    """
    Returns the version from the version info.
    """
    if __version_info__['releaselevel'] not in ('alpha', 'beta', 'final'):
        raise ValueError(
            "unknown release level '{}', select alpha, beta, or final.".format(
                __version_info__['releaselevel']
            )
        )

    vers = ["{major}.{minor}".format(**__version_info__)]

    if __version_info__['micro']:
        vers.append(".{micro}".format(**__version_info__))

    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('{}{}'.format(__version_info__['releaselevel'][0],
                                  __version_info__['serial']))

    return ''.join(vers)
