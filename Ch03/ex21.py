#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:45:13 2018

@author: vpapg
"""

# Write a function unknown() that takes a URL as its argument, and returns a list of unknown words that occur on that webpage. In order to do this, extract all substrings consisting of lowercase letters (using re.findall()) and remove any items from this set that occur in the Words Corpus (nltk.corpus.words). Try to categorize these words manually and discuss your findings.

from bs4 import BeautifulSoup
from urllib import request
import nltk, re

def unknown(url):
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html,"lxml").get_text()
    lower = re.findall(r'(?<= )+[a-z]+\b',raw[10021:11554])
    # (?<=B)A | Positive lookbehind assertion. This matches the expression A only if B is immediately to its left. This can only match fixed length expressions.
    words = nltk.corpus.words.words()
    l = [w for w in lower if w not in words]
    print(l)

unknown("https://en.wikipedia.org/wiki/Radiohead")