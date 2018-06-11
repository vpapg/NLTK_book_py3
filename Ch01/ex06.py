#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 23:15:17 2018

@author: vpapg
"""

# Produce a dispersion plot of the four main protagonists 
# in Sense and Sensibility: Elinor, Marianne, Edward, and 
# Willoughby. What can you observe about the different roles 
# played by the males and females in this novel? Can you 
# identify the couples?

from nltk.book import *

text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])

# Females are referred more frequently.
# Elinor appears more times than anyone else.
# Noticing that there are cases where Edward's name is referred but Marianne's isn't, 
#it can be inferred that Elinor and Edward is the one couple
# and Marianne and Willoughby is the other.