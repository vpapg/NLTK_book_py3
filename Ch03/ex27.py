#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 01:25:42 2018

@author: vpapg
"""

# Python's random module includes a function choice() which randomly chooses an item from a sequence, e.g. choice("aehh ") will produce one of four possible characters, with the letter h being twice as frequent as the others. Write a generator expression that produces a sequence of 500 randomly chosen letters drawn from the string "aehh ", and put this expression inside a call to the ''.join() function, to concatenate them into one long string. You should get a result that looks like uncontrolled sneezing or maniacal laughter: he  haha ee  heheeh eha. Use split() and join() again to normalize the whitespace in this string.

from random import choice

s = ''.join(choice("aehh ") for i in range(500))
print(s,'\n')
s = ' '.join(s.split())
print(s)