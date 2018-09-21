#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:02:58 2018

@author: vpapg
"""

# Use the Porter Stemmer to normalize some tokenized text, calling the stemmer on each word. Do the same thing with the Lancaster Stemmer and see if you observe any differences.

import nltk

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
text = nltk.corpus.brown.words(categories='fiction')
text = text[:96]

p = [porter.stem(t) for t in text]
l = [lancaster.stem(t) for t in text]

for i in range(96):
    print(text[i],p[i],l[i])