#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:48:38 2018

@author: vpapg
"""

# Create a file consisting of words and (made up) frequencies, where each line consists of a word, the space character, and a positive integer, e.g. fuzzy 53. Read the file into a Python list using open(filename).readlines(). Next, break each line into its two fields using split(), and convert the number into an integer using int(). The result should be a list of the form: [['fuzzy', 53], ...].

freqs = open('frequencies.txt').readlines()

list = []

for element in freqs:
    temp = element.split(' ')
    list.append([temp[0], int(temp[1])])
    
print(list)