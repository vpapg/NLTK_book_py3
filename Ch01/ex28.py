#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 03:01:59 2018

@author: vpapg
"""

# Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.

from nltk.book import *

def percent(word, text):
    return 100 * text.count(word) / len(text)

print(percent('a',text4))