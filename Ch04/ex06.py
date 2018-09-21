#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:12:32 2018

@author: vpapg
"""

# Does the method for creating a sliding window of n-grams behave correctly for the two limiting cases: n = 1, and n = len(sent)?

sent = ['It', 'is', 'a', 'perfect', 'day', 'Elise']

for n in range(1,len(sent)+1):
    print([sent[i:i+n] for i in range(len(sent)-n+1)])
    print()