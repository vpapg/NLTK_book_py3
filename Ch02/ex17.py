#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:09:09 2018

@author: vpapg
"""

# Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

from nltk.corpus import stopwords
from nltk.book import *
from nltk.probability import FreqDist

def freq50(text):
    stop_words = stopwords.words('english')
    content = [w.lower() for w in text if w.lower() not in stop_words and w.isalpha()]
    fd = FreqDist(content)
    return [w for w, freq in fd.most_common(50)]

print(freq50(text1))
print()
print(freq50(text2))
print()
print(freq50(text3))
print()