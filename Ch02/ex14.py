#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 04:34:51 2018

@author: vpapg
"""

# Define a function supergloss(s) that takes a synset s as its argument and 
# returns a string consisting of the concatenation of the definition of s, and
# the definitions of all the hypernyms and hyponyms of s.

from nltk.corpus import wordnet as wn

def supergloss(s):
    st = 'DEFINITION: ' + s.definition() + '\n\n\nHYPERNYMS:'
    for i in s.hypernyms():
        st = st + '\n' + i.name().upper() + ': ' + i.definition() + '\n'
    st += '\n\nHYPONYMS:'
    for i in s.hyponyms():
        st = st + '\n' + i.name().upper() + ': ' + i.definition() + '\n'
    return st

print(supergloss(wn.synset('tree.n.01')))


# OR
'''
def supergloss(s):
    st = s.definition()
    for i in s.hypernyms():
        st = st + '\n' + i.definition()
    for i in s.hyponyms():
        st = st + '\n' + i.definition()
    return st
'''