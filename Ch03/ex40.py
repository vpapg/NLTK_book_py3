#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 21:17:25 2018

@author: vpapg
"""

# Obtain raw texts from two or more genres and compute their respective reading difficulty scores as in the earlier exercise on reading difficulty. E.g. compare ABC Rural News and ABC Science News (nltk.corpus.abc). Use Punkt to perform sentence segmentation.

from nltk.corpus import abc
from nltk import word_tokenize, sent_tokenize


abc_rural = abc.raw("rural.txt")
abc_science = abc.raw("science.txt")


def ARI(raw):
    words = word_tokenize(raw)
    sents = sent_tokenize(raw) # I used different method for sentence segmentation
    mw = sum(len(w) for w in words)/len(words)
    ms = sum(len(s) for s in sents)/len(sents)
    return 4.71 * mw + 0.5 * ms - 21.43

print(ARI(abc_rural))
print(ARI(abc_science))