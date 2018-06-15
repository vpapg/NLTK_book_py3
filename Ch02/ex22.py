#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:20:43 2018

@author: vpapg
"""

# Define a function hedge(text) which processes a text and produces a new version with the word 'like' between every third word.

def hedge(text):
    i=0
    final = []
    if type(text) is str:
        text = text.split()
    for w in text:
        final.append(w)
        if i==2:
            final.append('like')
            i=0
        else:
            i+=1
    return ' '.join(final) # OR "return final" as a list

print(hedge("Come together right now over me"))

print(hedge(["Come", "together", "right", "now", "over", "me"]))