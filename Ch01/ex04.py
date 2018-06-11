#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:15:17 2018

@author: vpapg
"""

# Review 1 on computing with language. 
# How many words are there in text2?
# How many distinct words are there?

from nltk.book import *

# print words
print("Words:", len(text2))

# print distinct words
print("Distinct words:", len(set(text2)))