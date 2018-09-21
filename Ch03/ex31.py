#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:15:51 2018

@author: vpapg
"""

# Define the variable saying to contain the list ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']. Process this list using a for loop, and store the length of each word in a new list lengths. Hint: begin by assigning the empty list to lengths, using lengths = []. Then each time through the loop, use append() to add another length value to the list. Now do the same thing using a list comprehension.

saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more',
'is', 'said', 'than', 'done', '.']

lengths1 = []

for w in saying:
    lengths1.append(len(w))
    
lengths2 = [len(w) for w in saying]

print(lengths1)
print(lengths2)