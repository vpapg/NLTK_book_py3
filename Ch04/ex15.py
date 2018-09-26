#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:01:34 2018

@author: vpapg
"""

# Write a program that takes a sentence expressed as a single string, splits it and counts up the words. Get it to print out each word and the word's frequency, one per line, in alphabetical order.

sent = 'I love living in Sheffield and you love me and she loves us'

tokens = sent.split()
counts = sorted(set([(t, tokens.count(t)) for t in tokens]))

for i in counts:
    print(i[0] + ': ', i[1])




# Initially I had mistakenly used the length of each word:

'''
# implemented step by step:

tokens = sent.split()
tokens_count = [len(t) for t in tokens]

zipped = sorted(zip(tokens, tokens_count))
'''



'''
# implemented in one line:
zipped = sorted(zip(sent.split(), [len(t) for t in sent.split()]))



for t in zipped:
    print(t[0] + ': ', t[1])
'''