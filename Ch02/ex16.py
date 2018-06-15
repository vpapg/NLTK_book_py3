#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 06:33:09 2018

@author: vpapg
"""

# Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in 1.1. Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()). Which genre has the lowest diversity (greatest number of tokens per type)? Is this what you would have expected?

from nltk.corpus import brown
from tabulate import tabulate

def lexical_diversity(text):
    return len(set(text)) / len(text)

table = [["news",lexical_diversity(brown.words(categories="news"))],
         ["religion",lexical_diversity(brown.words(categories="religion"))],
         ["hobbies",lexical_diversity(brown.words(categories="hobbies"))],
         ["science_fiction",lexical_diversity(brown.words(categories="science_fiction"))],
         ["romance",lexical_diversity(brown.words(categories="romance"))],
         ["humor",lexical_diversity(brown.words(categories="humor"))]]

print(tabulate(table))