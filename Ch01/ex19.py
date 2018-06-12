#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:56:10 2018

@author: vpapg
"""

# What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?
# sorted(set(w.lower() for w in text1))
# sorted(w.lower() for w in set(text1))


# first transforms the words to lowercase and then keeps the distinct words. So occurrences with previously uppercase letters are not included.
print(len(sorted(set(w.lower() for w in text1)))) # less
print()
# first keeps the distinct words and then transforms then into lowercase. So occurrences with previously uppercase letters are included.
print(len(sorted(w.lower() for w in set(text1)))) # more

# One exception: if the text contains ONLY uppercase/lowercase. Then, they will have the same length.