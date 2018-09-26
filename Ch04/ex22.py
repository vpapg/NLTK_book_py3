#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 01:05:14 2018

@author: vpapg
"""

# Import the itemgetter() function from the operator module in Python's standard library (i.e. from operator import itemgetter). Create a list words containing several words. Now try calling: sorted(words, key=itemgetter(1)), and sorted(words, key=itemgetter(-1)). Explain what itemgetter() is doing.

from operator import itemgetter

words = ['text', 'set', 'argument', 'vocabulary', 'function', 'return', 'word', 'words', 'appear', 'text']

# Sorting according to the 2nd letter
print(sorted(words, key=itemgetter(1)))
print()

# Sorting according to the last letter
print(sorted(words, key=itemgetter(-1)))