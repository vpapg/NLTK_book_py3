#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:19:31 2018

@author: vpapg
"""

# Define a variable silly to contain the string: 'newly formed bland ideas are inexpressible in an infuriating way'. (This happens to be the legitimate interpretation that bilingual English-Spanish speakers can assign to Chomsky's famous nonsense phrase, colorless green ideas sleep furiously according to Wikipedia). Now write code to perform the following tasks:
#
#  a. Split silly into a list of strings, one per word, using Python's split() operation, and save this to a variable called bland.
#  b. Extract the second letter of each word in silly and join them into a string, to get 'eoldrnnnna'.
#  c. Combine the words in bland back into a single string, using join(). Make sure the words in the resulting string are separated with whitespace.
#  d. Print the words of silly in alphabetical order, one per line.

silly = '''newly formed bland ideas are inexpressible in an infuriating
way'''

bland = silly.split()

str_b = ''.join([w[1] for w in bland])

str_c = ' '.join(bland)

print(silly,'\n')
print(bland,'\n')
print(str_b,'\n')
print(str_c,'\n')
for w in sorted(bland):
    print(w)