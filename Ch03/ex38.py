#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:30:12 2018

@author: vpapg
"""

# An interesting challenge for tokenization is words that have been split across a line-break. E.g. if long-term is split, then we have the string long-\nterm.

#  a. Write a regular expression that identifies words that are hyphenated at a line-break. The expression will need to include the \n character.
#  b. Use re.sub() to remove the \n character from these words.
#  c. How might you identify words that should not remain hyphenated once the newline is removed, e.g. 'encyclo-\npedia'?x

import re
from nltk.corpus import words

vocabulary = words.words()

text = "There is no denying that this encyclo-\npedia is one of the best you can find! Oh, but we were dis-\ncussing about your long-\nterm plans, right?"

a = re.findall(r'\w+\-\n\w+', text)
b = [re.sub(r'\n', '', w.lower()) for w in a]

print('Text:',text,'\n')
print('(a):',a)
print()
print('(b):',b)
print()

c=[]

'''
# It doesn't work because not every word is included in the vocabulary
for w in b:
    if re.sub(r'\-', '', w) in vocabulary:
        c.append(re.sub(r'\-', '', w))
    else:
        c.append(w)
        
print(w)
'''

for w in b:
    w_part = w.split('-')
    if w_part[0] in vocabulary and w_part[1] in vocabulary:
        c.append(w)
    else:
        c.append(re.sub(r'\-', '', w))

print('(c):',c)