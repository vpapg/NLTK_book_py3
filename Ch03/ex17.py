#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 22:16:14 2018

@author: vpapg
"""

# What happens when the formatting strings %6s and %-6s are used to display strings that are longer than six characters?

print("%6s" % 'Hi') # Characters 0-4 are whitespaces, 5-6 are "Hi"
print("%-6s" % 'Hi') # Normal
print()
print("%6s" % '123456') # Normal
print("%-6s" % '123456') # Normal
print()
print("%6s" % '12345678') # Normal
print("%-6s" % '12345678') # Normal