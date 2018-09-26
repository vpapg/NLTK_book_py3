#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 00:30:29 2018

@author: vpapg
"""

# Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by decreasing frequency. E.g. if the input list contained 10 instances of the word table and 9 instances of the word chair, then table would appear before chair in the output list.


def sortedset(wordlist):
    l = sorted(set([(wordlist.count(w), w) for w in [wlower.lower() for wlower in wordlist]]), reverse=True)
    return [element[1] for element in l]

words = ['Karma', 'police', 'arrest', 'this', 'man', 'and', 'arrest', 'this', 'girl']

print(sortedset(words))

# l = set(sorted(...)) doesn't work, because set() changes the word order. So, I counted their instances, deleted duplicated with set(), and then according to their number of instances I sorted them and returned them without their counts.