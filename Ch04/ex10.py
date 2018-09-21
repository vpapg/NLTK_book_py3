#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:32:38 2018

@author: vpapg
"""

# Write a program to sort words by length. Define a helper function cmp_len which uses the cmp comparison function on word lengths.

words = ['declare', 'this', 'an', 'emergency', 'come', 'on', 'and', 'spread', 'a', 'sense', 'of', 'urgency', 'and', 'pull', 'us', 'through']

# cmp is not a built-in function in Python 3.x

print(words)
print()
print(sorted(words, key=len))
