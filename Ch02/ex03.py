#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:12:42 2018

@author: vpapg
"""

# Use the Brown corpus reader nltk.corpus.brown.words() or the Web text corpus 
# reader nltk.corpus.webtext.words() to access some sample text in two 
# different genres.

from nltk.corpus import brown, webtext

b_words1 = brown.words(categories='romance')
b_words2 = brown.words(categories='humor')
w_words = webtext.words()

print(b_words1[155:218],'\n')
print(b_words2[476:515],'\n')
print(w_words[95:180])