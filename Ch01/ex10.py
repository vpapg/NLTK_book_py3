#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:09:01 2018

@author: vpapg
"""

# Define a variable my_sent to be a list of words, using the syntax my_sent = ["My", "sent"] (but with your own words, or a favorite saying).
#
# a. Use ' '.join(my_sent) to convert this into a string.
#
# b. Use split() to split the string back into the list form you had to start with.

my_sent = ["Karma", "police", "arrest", "this", "man", "he", "talks", "in", "maths"]
print(my_sent)

print("\nQuestion (a)\n")
my_string = ' '.join(my_sent)
print(my_string)

print("\n\nQuestion (b)\n")
print(my_string.split())