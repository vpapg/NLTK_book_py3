#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:01:49 2018

@author: vpapg
"""

# Read about the built-in comparison function cmp, by typing help(cmp). How does it differ in behavior from the comparison operators?


# cmp does not exist in Python 3.x. What can be done istead is:

def cmp(a, b):
    return (a > b) - (a < b) 

print(cmp(5,2), 5>=2)
print(cmp(2,5), 2>5)
print(cmp(2,2), 2>=2)
print(cmp(2,2), 2==2)

# or, alternatively, import operator and use eg(), lt(), gt()