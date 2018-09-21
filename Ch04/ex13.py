#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:35:48 2018

@author: vpapg
"""

# Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.

import re 

words = ['transport', 'motorways', 'tramlines', 'starting', 'stopping']
   
word_vowels = [{len(w),len(re.findall(r'[aeiou]',w))} for w in words]

print(words)
print(word_vowels)

print('\nType of word_vowels:  ', type(word_vowels))
print('Type of elements in word_vowels:  ', type(word_vowels[0]))
