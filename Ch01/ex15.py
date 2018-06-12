#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:39:13 2018

@author: vpapg
"""

# Review the discussion of conditionals in 4. Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.

from nltk.book import *

b_words = [w for w in text5 if w.startswith('b') or w.startswith('B')]

print(sorted(set(b_words)))
# 'set' because there are multiple occurrences of the same words