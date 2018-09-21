#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 01:03:20 2018

@author: vpapg
"""

# Rewrite the following nested loop as a nested list comprehension:
#
#
#     words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
#     vsequences = set()
#     for word in words:
#         vowels = []
#         for char in word:
#             if char in 'aeiou':
#                 vowels.append(char)
#         vsequences.add(''.join(vowels))
#     sorted(vsequences)
# ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa']

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']

vsequences = [''.join([char for char in word if char in 'aeiou']) for word in words]

print(sorted(vsequences))