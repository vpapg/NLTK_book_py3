#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:16:24 2018

@author: vpapg
"""

# Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form whole sentences. What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?

phrase1 = "Hey Jude don't make it bad "
phrase2 = "Take a sad song and make it better "
phrase3 = "Remember to let her into your heart "
phrase4 = "Then you can start to make it better "

print("Phrase 1:", phrase1)
print("Phrase 2:", phrase2)
print("Phrase 3:", phrase3)
print("Phrase 4:", phrase4)

print()
print("1+2:")
print(print(phrase1+phrase2),len(phrase1+phrase2), len(phrase1) + len(phrase2))

print()
print("2+4:")
print(print(phrase2+phrase4),len(phrase2+phrase4), len(phrase2) + len(phrase4))


# same result, but:
#
# len(phrase1 + phrase2) first concatenates the strings and then calculates the length of the final string
#
# len(phrase1) + len(phrase2) doesn't concatenate the strings; it only adds their lengths