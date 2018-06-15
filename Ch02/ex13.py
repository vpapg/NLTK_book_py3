#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 04:27:05 2018

@author: vpapg
"""

# What percentage of noun synsets have no hyponyms? You can get all noun 
# synsets using wn.all_synsets('n').

from nltk.corpus import wordnet as wn

no_hyponyms = [w for w in wn.all_synsets('n') if len(w.hyponyms())==0]
noun_synsets = [w for w in wn.all_synsets('n')]

print("Percentage of noun synsets that have no hyponyms:", 
      len(no_hyponyms)*100/len(noun_synsets))