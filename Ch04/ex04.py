#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:54:38 2018

@author: vpapg
"""

# Create a list words = ['is', 'NLP', 'fun', '?']. Use a series of assignment statements (e.g. words[1] = words[2]) and a temporary variable tmp to transform this list into the list ['NLP', 'is', 'fun', '!']. Now do the same transformation using tuple assignment.

words = ['is', 'NLP', 'fun', '?']
print(words)

# Using assignment statements and a temp variable
tmp = words[0]
words[0] = words[1]
words[1] = tmp
words[3] = '!'
print(words)

words = ['is', 'NLP', 'fun', '?']

# Using tuple assignment
words[0], words[1], words[3] = words[1], words[0], '!'
print(words)