#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os, os.path
import sys
import re
from pprint import pprint, pformat

import plugs
for name, mod in plugs.store.items():
    print(name, ': ', sep='', end='')
    mod.run()

