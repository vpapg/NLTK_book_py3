#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 17:47:31 2018

@author: vpapg
"""

# Save some text into a file corpus.txt. Define a function load(f) that reads from the file named in its sole argument, and returns a string containing the text of the file.
#
#  a. Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the various kinds of punctuation in this text. Use one multi-line regular expression, with inline comments, using the verbose flag (?x).
#  b. Use nltk.regexp_tokenize() to create a tokenizer that tokenizes the following kinds of expression: monetary amounts; dates; names of people and organizations.

import nltk

def load(f):
    return open(f).read()

text = load('corpus.txt')
pattern = r'''(?x)
[.,;"'?\(\):\-_`]'''

print(text)
print()
print(nltk.regexp_tokenize(text,pattern))