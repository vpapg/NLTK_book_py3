#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:19:40 2018

@author: vpapg
"""

# Use the corpus module to explore austen-persuasion.txt. How many word tokens does this book have? How many word types?

from nltk.corpus import gutenberg

text = gutenberg.words('austen-persuasion.txt')

print(len(text), "word tokens.")
print(len(set(text)), "word types.")

print(len(set([w.lower() for w in text])), "word types (lowercased).")
print(len(set([w.lower() for w in text if w.isalpha()])), "word types (lowercased & alphanumeric).")