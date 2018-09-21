#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:05:06 2018

@author: vpapg
"""

# Readability measures are used to score the reading difficulty of a text, for the purposes of selecting texts of appropriate difficulty for language learners. Let us define μw to be the average number of letters per word, and μs to be the average number of words per sentence, in a given text. The Automated Readability Index (ARI) of the text is defined to be: 4.71 μw + 0.5 μs - 21.43. Compute the ARI score for various sections of the Brown Corpus, including section f (lore) and j (learned). Make use of the fact that nltk.corpus.brown.words() produces a sequence of words, while nltk.corpus.brown.sents() produces a sequence of sentences.

from nltk.corpus import brown

def ARI(cat):
    words = brown.words(categories=cat)
    sents = brown.sents(categories=cat)
    mw = sum(len(w) for w in words)/len(words)
    ms = sum(len(s) for s in sents)/len(sents)
    return 4.71 * mw + 0.5 * ms - 21.43

print('lore:',ARI('lore'))
print('learned:',ARI('learned'))

print('adventure:',ARI('adventure'))
print('belles_lettres:',ARI('belles_lettres'))
print('editorial:',ARI('editorial'))
print('fiction:',ARI('fiction'))
print('government:',ARI('government'))
print('hobbies:',ARI('hobbies'))
print('humor:',ARI('humor'))
print('mystery:',ARI('mystery'))
print('news:',ARI('news'))
print('religion:',ARI('religion'))
print('reviews:',ARI('reviews'))
print('romance:',ARI('romance'))
print('science_fiction:',ARI('science_fiction'))