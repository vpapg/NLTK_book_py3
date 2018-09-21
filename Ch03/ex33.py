#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:27:54 2018

@author: vpapg
"""

# The index() function can be used to look up items in sequences. For example, 'inexpressible'.index('e') tells us the index of the first position of the letter e.
#
#  a. What happens when you look up a substring, e.g. 'inexpressible'.index('re')?
#  b. Define a variable words containing a list of words. Now use words.index() to look up the position of an individual word.
#  c. Define a variable silly as in the exercise above. Use the index() function in combination with list slicing to build a list phrase consisting of all the words up to (but not including) in in silly.

print('inexpressible'.index('e'))
print('Question a:', 'inexpressible'.index('re'))

words = ['I', 'am', 'dreaming', 'of', 'a', 'white', 'Christmas', 'just', 'like', 'the', 'ones', 'I', 'used', 'to', 'know']

print('Question b:',words.index('I'))

silly = '''newly formed bland ideas are inexpressible in an infuriating
way'''

bland = silly.split()

phrase = bland[:bland.index('in')]
print('Question c:',phrase)

# if we wanted to exclude only 'in' and phrase were a string instead of list:
#phrase = silly[:silly.index(' in ')]+silly[silly.index(' in ')+3:]
#
#print(phrase)