#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from importlib import import_module
import os, os.path

store = {}
for file in os.listdir(os.path.dirname(__file__)):
    if file != '__init__.py' and file.endswith('.py'):
        mod_name = file[:-3]
        mod = __import__(mod_name, globals(), locals())
        store[mod_name] = mod

