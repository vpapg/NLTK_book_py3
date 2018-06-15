#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:30:54 2018

@author: vpapg
"""

# Write a function word_freq() that takes a word and the name of a section of the Brown Corpus as arguments, and computes the frequency of the word in that section of the corpus.

from nltk.corpus import brown
import nltk

def word_freq(word, name):
    text = brown.words(categories=name)
    content = [w.lower() for w in text]
    fd = nltk.FreqDist(content)
    return fd[word]

print(word_freq('funny','humor'))
print(word_freq('why','mystery'))
print(word_freq('song','reviews'))
print(word_freq('bed','romance'))