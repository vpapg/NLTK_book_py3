#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 03:13:38 2018

@author: vpapg
"""

# We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1). Experiment with this using different arguments to set(). What does it do? Can you think of a practical application for this?

from nltk.book import *

print(set(sent3)<set(text1))

# it compares the number of distinct words of two lists

# larger lists do not necessarily contain more distinct words