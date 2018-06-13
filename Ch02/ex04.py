#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:30:48 2018

@author: vpapg
"""

# Read in the texts of the State of the Union addresses, using the state_union
# corpus reader. Count occurrences of men, women, and people in each document.
# What has happened to the usage of these words over time?

from nltk.corpus import state_union

text = state_union.words()
print("Men:", text.count("men"))
print("Women:", text.count("women"))

Text(text).dispersion_plot(["men", "women"])

cfd = nltk.ConditionalFreqDist(
        (target, fileid)
        for fileid in state_union.fileids()
        for w in state_union.words(fileid)
        for target in ['men', 'women']
        if w.lower().startswith(target))
cfd.plot()

# The word 'women' appears more in recent documents, so it appears more
# over time