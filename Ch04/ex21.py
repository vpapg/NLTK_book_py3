#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 00:47:57 2018

@author: vpapg
"""

# Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary. Both arguments can be represented as lists of strings. Can you do this in a single line, using set.difference()?

def wordsnotinvoc(text, voc):
    return set([w.lower() for w in text.split()]).difference(set(voc))

t = "Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text but not in the vocabulary."

vocabulary = ['text', 'set', 'argument', 'vocabulary', 'function', 'return', 'word', 'words', 'appear']

print(wordsnotinvoc(t,vocabulary))
