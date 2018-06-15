#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 04:56:44 2018

@author: vpapg
"""

# Write a program to find all words that occur at least three times in the Brown Corpus.

from nltk.corpus import brown
from nltk.probability import FreqDist

words = set([w.lower() for w in brown.words()])

fd = FreqDist([w.lower() for w in brown.words()])

x = [w for w in words if fd[w]>2]

print(len(x),'words appear at least three times.')
print('E.g.:', x[:10])