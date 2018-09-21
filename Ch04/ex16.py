#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:14:51 2018

@author: vpapg
"""

# Read up on Gematria, a method for assigning numbers to words, and for mapping between words having the same number to discover the hidden meaning of texts (http://en.wikipedia.org/wiki/Gematria, http://essenes.net/gemcal.htm).
#
#  a. Write a function gematria() that sums the numerical values of the letters of a word, according to the letter values in letter_vals:
#      	
#
#    >>> letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
#    ... 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
#    ... 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
#
#  b. Process a corpus (e.g. nltk.corpus.state_union) and for each document, count how many of its words have the number 666.
#
#  c. Write a function decode() to process a text, randomly replacing words with their Gematria equivalents, in order to discover the "hidden meaning" of the text.

import re
from nltk.corpus import state_union

# (a)
def gematria(word):
    
    letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
    
    return sum(letter_vals[l.lower()] for l in word if len(re.findall(r'[a-z]', l.lower())) > 0)


print('(a)\ngematria for \'forbidden\':', gematria('forbidden'), '\n\n')



# (b)
words = state_union.words()

#print('\n(b)\nNumber of words with gematria score 666: ' + str(len([w for w in words if (gematria(w)==666)])))

#w666 = [(fileid,w) for fileid in state_union.fileids() for w in state_union.words(fileid) if gematria(w)==666]

print('(b)')
for fileid in state_union.fileids():
    w666 = [w.lower() for w in state_union.words(fileid) if gematria(w)==666]
    print(fileid, ': ', len(w666), w666)
    print()



# (c)
def decode(text):
    tokens = [t.lower() for t in text.split()]
    codes = [str(gematria(t)) for t in tokens]
    return ' '.join(codes)

text = 'I love listening to music all day'
print('\n\n(c)')
print(text)
print(decode(text))
