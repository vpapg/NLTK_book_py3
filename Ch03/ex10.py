#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:42:14 2018

@author: vpapg
"""

sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']

result = []

for word in sent:
    word_len = (word, len(word))
    result.append(word_len)

print(result)

print()
res = [(w,len(w)) for w in sent]
print(res)