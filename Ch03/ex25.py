#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:49:47 2018

@author: vpapg
"""

# Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin
#
#  a. Write a function to convert a word to Pig Latin.
#  b. Write code that converts text, instead of individual words.
#  c. Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).

from nltk import word_tokenize
import re

def wordToPigLatin(word):
    pig = re.findall(r'^([bcdfghjklmnpqrstvwxz]+|y)(.+)$', word)
    for (a,b) in pig:
        word = b+a
    word += 'ay'
    return word

print('drums ->', wordToPigLatin('drums'))
print('\ncriminology ->', wordToPigLatin('criminology'))
print('\nanimation ->', wordToPigLatin('animation'))


def strToPigLatin(string):
    l = word_tokenize(string)
    str_return = ''
    for word in l:
        str_return += wordToPigLatin(word) + ' '
    return str_return

print('\nhello darkness my old friend ->', strToPigLatin('hello darkness my old friend'))

print('\nyellow ->', wordToPigLatin('yellow'))
print('\ndye ->', wordToPigLatin('dye'))