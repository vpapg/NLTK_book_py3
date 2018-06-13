#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:56:43 2018

@author: vpapg
"""

# Create a variable phrase containing a list of words. Review the operations described in the previous chapter, including addition, multiplication, indexing, slicing, and sorting.

phrase = ['And', 'I', 'think', 'to', 'myself', 'what', 'a', 'wonderful', 'world']

print("----------------Addition----------------")
print(phrase[0]+' '+phrase[6]+' '+phrase[7]+' '+phrase[8])
print()

print("-------------Multiplication-------------")
print((phrase[7]+' ')*3+phrase[8]) # with addition
print()

print("----------------Indexing----------------")
print(phrase[2])
print(phrase.index('think'))
print(phrase[-2])
print()

print("----------------Slicing----------------")
print(phrase[1:3])
print(phrase[-2:])
print()

print("----------------Sorting----------------")
print(sorted(phrase)) # uppercase are first
print()
print(sorted(phrase, key=lambda w: w.casefold())) # uppercase not first, without making them lowercase
print()
print()
print(sorted(phrase, reverse=True)) # uppercase last
print()
print(sorted(phrase, reverse=True, key=lambda w: w.casefold())) # uppercase not last, without making them lowercase