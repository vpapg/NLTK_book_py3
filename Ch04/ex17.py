#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 02:27:39 2018

@author: vpapg
"""

# Write a function shorten(text, n) to process a text, omitting the n most frequently occurring words of the text. How readable is it?

from nltk import FreqDist

def shorten(text,n):
    words = [w.lower() for w in text.split()]
    most_freq = [x[0] for x in FreqDist(words).most_common(n)]
    return ' '.join([w for w in text.split() if w.lower() not in most_freq])

text = "A grandson of the philosopher Moses Mendelssohn, Felix Mendelssohn was born into a prominent Jewish family. He was brought up without religion until the age of seven, when he was baptised as a Reformed Christian. Felix was recognised early as a musical prodigy, but his parents were cautious and did not seek to capitalise on his talent. Mendelssohn enjoyed early success in Germany, and revived interest in the music of Johann Sebastian Bach, notably with his performance of the St Matthew Passion in 1829. He became well received in his travels throughout Europe as a composer, conductor and soloist; his ten visits to Britain  – during which many of his major works were premiered – form an important part of his adult career. His essentially conservative musical tastes set him apart from more adventurous musical contemporaries such as Franz Liszt, Richard Wagner, Charles-Valentin Alkan and Hector Berlioz. The Leipzig Conservatoire, which he founded, became a bastion of this anti-radical outlook."

print(shorten(text,5))