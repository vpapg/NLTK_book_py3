#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:27:56 2018

@author: vpapg
"""

# Define a string s = 'colorless'. Write a Python statement that changes this to "colourless" using only the slice and concatenation operations.

s = 'colorless'

s2 = s[:4] + 'u' + s[4:]

print(s2)