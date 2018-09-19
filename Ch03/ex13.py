#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:46:52 2018

@author: vpapg
"""

# What is the difference between calling split on a string with no argument or with ' ' as the argument, e.g. sent.split() versus sent.split(' ')? What happens when the string being split contains tab characters, consecutive space characters, or a sequence of tabs and spaces? (In IDLE you will need to use '\t' to enter a tab character.)

s = "Every time   I close my eyes\nit's like a dark paradise\tnothing compares to you\t\tblahblah"

print(s.split())
print()
print(s.split(' '))