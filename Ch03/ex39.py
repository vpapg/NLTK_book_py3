#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:14:06 2018

@author: vpapg
"""

# Read the Wikipedia entry on Soundex. Implement this algorithm in Python.

import re

def consToDigit(word):
    word = word.capitalize()
    w = re.sub(r'b|f|p|v', '1', word)
    w = re.sub(r'c|g|j|k|q|s|x|z', '2', w)
    w = re.sub(r'd|t', '3', w)
    w = re.sub(r'l', '4', w)
    w = re.sub(r'm|n', '5', w)
    w = re.sub(r'r', '6', w)
    while len(w)<4:
        w+='0'
    return w[:4]


def soundex(name):

    l = [['b','f','p','v'], ['c','g','j','k','q','s','x','z'], ['d','t'], ['l'], ['m','n'], ['r']]
    
    name = re.sub(r'[hw]', '', name)
    name = name.lower()
    for i in range(len(name)-2):
        for j in range(6):
            if name[i] in l[j] and name[i+1] in l[j]:
                name = name[:i] + name[i+1:]
    
    w = name[0]
    name = name[1:]
    w += re.sub(r'[aeiouy]', '', name)
    
    return consToDigit(w)
    
    
    
    
text = "Robert Rupert Rubin Ashcraft Ashcroft Tymczak Pfister Honeyman White"

textlist = text.split()

for name in textlist:
    print(name, soundex(name))