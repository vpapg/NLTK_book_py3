#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 01:58:26 2018

@author: vpapg
"""

'''
Define a function find_language() that takes a string as its argument, and returns a list of languages that have that string as a word. Use the udhr corpus and limit your searches to files in the Latin-1 encoding.
'''

from nltk.corpus import udhr
def find_language(word):
    lang = [fileid[:-7] for fileid in udhr.fileids() if fileid.endswith('-Latin1') and word in udhr.words(fileid)]
    return lang
            
print('on:', find_language('on'),'\n')
print('when:', find_language('when'),'\n')
print('love:', find_language('love'),'\n')
print('bien:', find_language('bien'),'\n')
print('gut:', find_language('gut'),'\n')