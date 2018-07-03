#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 00:24:09 2018

@author: vpapg
"""

'''
Modify the text generation program in 2.2 further, to do the following tasks:

a. Store the n most likely words in a list words then randomly choose a word from the list using random.choice(). (You will need to import random first.)

b. Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts. Train the model on this corpus and get it to generate random text. You may have to experiment with different start words. How intelligible is the text? Discuss the strengths and weaknesses of this method of generating random text.

c. Now train your system using two distinct genres and experiment with generating text in the hybrid genre. Discuss your observations.
'''

import random, nltk

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()

text1 = nltk.corpus.genesis.words('english-kjv.txt')
text2 = nltk.corpus.brown.words(categories='romance')

bigrams = []

bigrams.extend(nltk.bigrams(text1))
bigrams.extend(nltk.bigrams(text2))
cfd = nltk.ConditionalFreqDist(bigrams)


text = [w.lower() for w in text1 if w.isalpha()]
text.extend([w.lower() for w in text2 if w.isalpha()])
fdist = nltk.FreqDist(w for w in text)
fdist_ordered = fdist.most_common(100)
words = [x for x,y in fdist_ordered]
rnd_word = random.choice(words)

generate_model(cfd, rnd_word)