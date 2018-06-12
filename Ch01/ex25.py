#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:47:28 2018

@author: vpapg
"""

# Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:
#
# a. Print all words beginning with sh
# b. Print all words longer than four characters

from nltk.book import *

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

print([w for w in sent if w.startswith('sh')])
print()
print([w for w in sent if len(w)>4])