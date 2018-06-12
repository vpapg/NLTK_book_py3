#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 02:50:51 2018

@author: vpapg
"""

# What does the following Python code do?
# sum(len(w) for w in text1)
# Can you use it to work out the average word length of a text?

from nltk.book import *

# it returns the sum of the lengths of the words of text1

#average word length:
print(sum(len(w) for w in text1)/len(text1))