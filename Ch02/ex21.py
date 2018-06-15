#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:33:45 2018

@author: vpapg
"""

# Write a program to guess the number of syllables contained in a text, making use of the CMU Pronouncing Dictionary.

from nltk.corpus import cmudict
from nltk.book import *

prondict = cmudict.dict()

syllables = 0

#text1 = ["Hello", "how", "are", "you"]

for w in text1:
    if w.isalpha() and w.lower() in prondict:
        for ph in prondict[w.lower()][0]: #[0] in order to get only one of the multiple possible pronunciations
            if any(char.isdigit() for char in ph):
                syllables += 1

print(syllables)
