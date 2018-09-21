#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 01:01:54 2018

@author: vpapg
"""

# Download some text from a language that has vowel harmony (e.g. Hungarian), extract the vowel sequences of words, and create a vowel bigram table.

from nltk.corpus import brown
from nltk import ConditionalFreqDist, Index
import re

romance = brown.words(categories='romance')

vowel_seqs_list = [(vowels_set, w) for w in romance for vowels_set in re.findall(r'[aeiou][aeiou]', w)]
vowel_seqs_index = Index(vowel_seqs_list)
#print(vowel_seqs_index['aa'])

l=[]
for element in vowel_seqs_list:
    l.append(element[0])

cfd = ConditionalFreqDist(l)
cfd.tabulate()