#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:15:17 2018

@author: vpapg
"""

# Compare the lexical diversity scores for humor and romance 
# fiction in 1.1. Which genre is more lexically diverse?

from nltk import corpus

def lexical_diversity(text):
    return len(set(text)) / len(text)

humor_words = corpus.brown.words(categories="humor")
romance_words = corpus.brown.words(categories="romance")

print("Humor:",lexical_diversity(humor_words))
print("Romance:",lexical_diversity(romance_words))