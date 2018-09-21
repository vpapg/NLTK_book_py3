#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:18:26 2018

@author: vpapg
"""

# Write code that removes whitespace at the beginning and end of a string, and normalizes whitespace between words to be a single space character.
#
#  1. do this task using split() and join()
#  2. do this task using regular expression substitutions

import re

s = " While you are away,  my heart comes undone,  slowly unravels  in a ball of yarn.  The devil collects it  with a grin.  Our love  in a ball of yarn.   He'll never return it..."

cleared1 = ' '.join(s.split())
print(s + '\n\n' + cleared1)

cleared2 = re.sub(r'^ ', '', s)
cleared2 = re.sub(r' {2,}', ' ', cleared2)
print('\n' + cleared2)