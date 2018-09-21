#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:39:13 2018

@author: vpapg
"""

# Write code to convert nationality adjectives like Canadian and Australian to their corresponding nouns Canada and Australia (see http://en.wikipedia.org/wiki/List_of_adjectival_forms_of_place_names).

def convertToNoun(adjective):
    if adjective.endswith('dian'):
        return adjective[:-3]+'a'
    elif adjective=='European':
        return 'Europe'
    elif adjective=='Caribbean':
        return adjective
    elif adjective=='American':
        return 'Americas'
    elif adjective.endswith('Indian'):
        return adjective[:-6]+'Indies'
    elif adjective.endswith('an'):
        return adjective[:-1]
    elif adjective.endswith('ern'):
        return adjective[:-3]
    elif adjective=='Antarctic':
        return 'Antarctica'
    elif adjective.endswith('gish'):
        return adjective[:-3]
    else:
        return adjective


print(convertToNoun('Afro-Eurasian'))
print(convertToNoun('African'))
print(convertToNoun('Eurasian'))
print(convertToNoun('South-Australian'))
print(convertToNoun('Tasmanian'))
print(convertToNoun('Western Australian'))
print(convertToNoun('Nova Scotian'))
print(convertToNoun('Bavarian'))
print(convertToNoun('Brandenburgish'))
print(convertToNoun('Hamburgish'))

# checked on only some of the adjectives