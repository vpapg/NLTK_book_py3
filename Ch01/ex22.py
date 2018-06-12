#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:08:17 2018

@author: vpapg
"""

# Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

from nltk.book import *

# not 'set', in order to count the frequencies
words4 = [w.lower() for w in text5 if w.isalpha() and len(w)==4]

fd = FreqDist(words4)

# fd.N() returns the number of distinct words
# fd.pformat returns the words with their frequencies, in descending order. The argument expresses the max number of elements to be shown (default=10)
print(fd.pformat(fd.N()))