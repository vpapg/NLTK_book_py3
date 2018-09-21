#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 21:12:59 2018

@author: vpapg
"""

# Create a list of words and store it in a variable sent1. Now assign sent2 = sent1. Modify one of the items in sent1 and verify that sent2 has changed.
#
#  a. Now try the same exercise but instead assign sent2 = sent1[:]. Modify sent1 again and see what happens to sent2. Explain.
#  b. Now define text1 to be a list of lists of strings (e.g. to represent a text consisting of multiple sentences. Now assign text2 = text1[:], assign a new value to one of the words, e.g. text1[1][1] = 'Monty'. Check what this did to text2. Explain.
#  c. Load Python's deepcopy() function (i.e. from copy import deepcopy), consult its documentation, and test that it makes a fresh copy of any object.

from copy import deepcopy

sent1 = ['declare', 'this', 'an', 'emergency', 'come', 'on', 'and', 'spread', 'a', 'sense', 'of', 'urgency', 'and', 'pull', 'us', 'through'] 

sent2 = sent1
sent1[0] = 'DECLARE'

print(sent1)
print()
print(sent2)
print()
# sent2 is a copy of sent1 (assignment by reference, not by value)


# (a)
sent1 = ['declare', 'this', 'an', 'emergency', 'come', 'on', 'and', 'spread', 'a', 'sense', 'of', 'urgency', 'and', 'pull', 'us', 'through'] 

sent2 = sent1[:]
sent1[0] = 'DECLARE'

print('\n(a)\n')
print(sent1)
print()
print(sent2)
print()
# sent2 is assigned with the values elements of sent1 (assignment by value, not by reference)


# (b)
text1 = [['declare', 'this', 'an', 'emergency'],['come', 'on', 'and', 'spread', 'a', 'sense', 'of', 'urgency'], ['and', 'pull', 'us', 'through']]

text2 = text1[:]
text1[0][0] = 'DECLARE'

print('\n(b)\n')
print(text1)
print()
print(text2)
print()
# the outside list has its elements by value, but the elements are lists which are assigned by reference


# (c)
text1 = [['declare', 'this', 'an', 'emergency'],['come', 'on', 'and', 'spread', 'a', 'sense', 'of', 'urgency'], ['and', 'pull', 'us', 'through']]

text2 = deepcopy(text1)
text1[0][0] = 'DECLARE'

print('\n(c)\n')
print(text1)
print()
print(text2)
print()
