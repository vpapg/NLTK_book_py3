#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:38:05 2018

@author: vpapg
"""

# We can specify a "step" size for the slice. The following returns every second character within the slice: monty[6:11:2]. It also works in the reverse direction: monty[10:5:-2] Try these for yourself, then experiment with different step values.

bhsun = 'Black hole sun won\'t you come and wash away the rain'
print(bhsun)
print()
print(bhsun[::2])
print()
print(bhsun[3::3])
print()
print(bhsun[4:17:4])
print()
print(bhsun[17:4:-2])
print()
print()

monty = 'Monty Python'
print(monty[6:11:2])
print()
print(monty[10:5:-2])