#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
import sys

from webcompat import app

BOT_HELP = 'BOT OAUTH TOKEN NOT SET'


def config_validator():
    '''Make sure the config file is ready.'''
    # Checking if there is a bot configured
    if app.config['BOT_OAUTH_TOKEN'] == '':
        sys.exit(BOT_HELP)

if __name__ == '__main__':
    # testing the config file
    config_validator()
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--testmode', action='store_true',
                        help='Run server in "test mode".')
    args = parser.parse_args()

    if args.testmode:
        # disable HttpOnly setting for session cookies so Selenium
        # can interact with them. *ONLY* do this for testing.
        app.config['SESSION_COOKIE_HTTPONLY'] = False
        print("Starting server in ~*TEST MODE*~")
        app.run()
    else:
        app.run()
