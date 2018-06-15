#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 04:14:33 2018

@author: vpapg
"""

#12 The CMU Pronouncing Dictionary contains multiple pronunciations for certain words. How many distinct words does it contain? What fraction of words in this dictionary have more than one possible pronunciation?

from nltk.corpus import cmudict

words = [w for w, pron in cmudict.entries()]

words_distinct = set(words)
cmu = cmudict.dict()

print('Number of words:',len(words))
print('Number of distinct words:',len(words_distinct))
print()

pron_multi = [w for w in words_distinct if len(cmu.get(w))>1]
print(str(len(pron_multi)*100/len(words_distinct))+"% words have more than one possible pronunciation")