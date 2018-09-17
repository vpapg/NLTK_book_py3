#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:30:11 2018

@author: vpapg
"""

# Read in some text from a corpus, tokenize it, and print the list of all wh-word types that occur. (wh-words in English are used in questions, relative clauses and exclamations: who, which, what, and so on.) Print them in order. Are any words duplicated in this list, because of the presence of case distinctions or punctuation?

from nltk import corpus
import re

# Wh-words usually have a short length. However, words of short length that are not wh-words are also returned.
wh_words = set([w for w in corpus.gutenberg.words('melville-moby_dick.txt') if w.startswith('wh') and len(w)<6])
print(wh_words)


wh = set([w for w in corpus.gutenberg.words('melville-moby_dick.txt') if re.search('^wh(y|at|om|ose|ich|ere|en)$',w)])
print()
print(wh)