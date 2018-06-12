#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:55:42 2018

@author: vpapg
"""

# Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.

from nltk.book import *

def vocab_size(text):
    return len(set([w.lower() for w in text if w.isalpha()]))
    # or
    # return len(set([w for w in text]))
    # or
    # return len(set([w.lower() for w in text]))
    # or
    # return len(set([w for w in text if w.isalpha()]))
    #
    # it depends on what we want to do
    
print(vocab_size(text1))