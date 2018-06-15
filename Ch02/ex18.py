#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:16:38 2018

@author: vpapg
"""

# Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

from nltk.corpus import stopwords
from nltk.book import *
import nltk

def freq50_bigrams(text):
    stop_words = stopwords.words('english')
    content = [w.lower() for w in text]
    bigrams = [bigram for bigram in nltk.bigrams(content)
    if bigram[0] not in stop_words and bigram[1] not in stop_words and
    bigram[0].isalpha() and bigram[1].isalpha()]
    fd = nltk.FreqDist(bigrams)
    return [b for b, num in fd.most_common(50)]

print(freq50_bigrams(text1))

