#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:42:39 2018

@author: vpapg
"""

# Investigate the holonym-meronym relations for some nouns. Remember that there
# are three kinds of holonym-meronym relation, so you need to use:
# member_meronyms(), part_meronyms(), substance_meronyms(), member_holonyms(),
# part_holonyms(), and substance_holonyms().

from nltk.corpus import wordnet as wn

print("----------Water----------")
print(wn.synset('water.n.01').member_meronyms())
print(wn.synset('water.n.01').part_meronyms())
print(wn.synset('water.n.01').substance_meronyms())

print(wn.synset('water.n.01').member_holonyms())
print(wn.synset('water.n.01').part_holonyms())
print(wn.synset('water.n.01').substance_holonyms())
print()

print("----------Chair----------")
print(wn.synset('chair.n.01').member_meronyms())
print(wn.synset('chair.n.01').part_meronyms())
print(wn.synset('chair.n.01').substance_meronyms())

print(wn.synset('chair.n.01').member_holonyms())
print(wn.synset('chair.n.01').part_holonyms())
print(wn.synset('chair.n.01').substance_holonyms())
print()

print("----------Computer----------")
print(wn.synset('computer.n.01').member_meronyms())
print(wn.synset('computer.n.01').part_meronyms())
print(wn.synset('computer.n.01').substance_meronyms())

print(wn.synset('computer.n.01').member_holonyms())
print(wn.synset('computer.n.01').part_holonyms())
print(wn.synset('computer.n.01').substance_holonyms())
