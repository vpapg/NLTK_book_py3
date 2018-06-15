#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 02:55:02 2018

@author: vpapg
"""

# Define a conditional frequency distribution over the Names corpus that allows you to see which initial letters are more frequent for males vs. females

from nltk.corpus import names
import nltk

cfd = nltk.ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
        for name in names.words(fileid))

cfd.plot()