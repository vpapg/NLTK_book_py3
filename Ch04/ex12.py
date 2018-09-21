#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:31:42 2018

@author: vpapg
"""

# Initialize an n-by-m list of lists of empty strings using list multiplication, e.g. word_table = [[''] * n] * m. What happens when you set one of its values, e.g. word_table[1][2] = "hello"? Explain why this happens. Now write an expression using range() to construct a list of lists, and show that it does not have this problem.

n = 5
m = 6

word_table = [[''] * n] * m
print(word_table)
print()

word_table[1][2] = "hello"
print(word_table)
print()

print()
word_table = [['' for i in range(n)] for j in range(m)]
print(word_table)
print()

word_table[1][2] = "hello"
print(word_table)