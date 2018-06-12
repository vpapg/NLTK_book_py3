#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:40:07 2018

@author: vpapg
"""

# Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].
#
# a. Ending in ize
# b. Containing the letter z
# c. Containing the sequence of letters pt
# d. Having all lowercase letters except for an initial capital (i.e., titlecase)

from nltk.book import *

print([w for w in text6 if w.endswith('ize')])
print()
print([w for w in text6 if 'z' in w])
print()
print([w for w in text6 if 'pt' in w])
print()
print([w for w in text6 if w.istitle()])