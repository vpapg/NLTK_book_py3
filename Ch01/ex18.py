#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:49:11 2018

@author: vpapg
"""

# Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.


# case sensitive, includes symbols and numbers, as in examples
voc = sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))
print(voc)

# case sensitive, doesn't include symbols and numbers
print()
voc2 = [w for w in voc if w.isalpha()]
print(voc2)