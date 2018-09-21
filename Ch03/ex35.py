#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:10:51 2018

@author: vpapg
"""

# Read the LanguageLog post on phrases of the form as best as p can and as best p can, where p is a pronoun. Investigate this phenomenon with the help of a corpus and the findall() method for searching tokenized text described in 3.5. http://itre.cis.upenn.edu/~myl/languagelog/archives/002733.html

from nltk.corpus import brown, webtext
from nltk import Text

pronouns = ['i', 'you', 'he', 'she', 'it', 'we', 'they']

#text = Text([w.lower() for w in brown.words(categories='editorial')])
# no instances in any of the brown tried

text = Text([w.lower() for w in webtext.words()])

print('AS BEST AS:')
print(text.findall(r"<as> <best> <as> <.*> <can>"))

print('\n\nAS BEST:')
print(text.findall(r"<as> <best> <.*> <can>"))
