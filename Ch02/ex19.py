#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 07:24:18 2018

@author: vpapg
"""

# Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.

from nltk.corpus import brown
import nltk

cfd = nltk.ConditionalFreqDist(
        (genre, word.lower())
        for genre in brown.categories()
        for word in brown.words(categories=genre))
words = ['hurt','attack','financial','god','sport','spaceship','love','friend']
cfd.tabulate(conditions=brown.categories(), samples=words)
