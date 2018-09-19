#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:33:17 2018

@author: vpapg
"""

# We can use the slice notation to remove morphological endings on words. For example, 'dogs'[:-1] removes the last character of dogs, leaving dog. Use slice notation to remove the affixes from these words (we've inserted a hyphen to indicate the affix boundary, but omit this from your strings): dish-es, run-ning, nation-ality, un-do, pre-heat.

print('dishes'[:-2])
print('nationality'[:-5])
print('preheat'[3:])
print('running'[:-4])
print('undo'[2:])