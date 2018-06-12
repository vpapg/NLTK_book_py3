#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:29:21 2018

@author: vpapg
"""

# The first sentence of text3 is provided to you in the variable sent3. The index of the in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two other occurrences of this word in sent3?

from nltk.book import *

print([index for index in range(len(sent3)) if sent3[index] == 'the'])

# or
print()

for index in range(len(sent3)):
    if sent3[index] == 'the':
        print(index)