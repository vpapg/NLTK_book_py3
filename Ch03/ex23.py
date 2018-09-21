#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:26:21 2018

@author: vpapg
"""

# Are you able to write a regular expression to tokenize text in such a way that the word don't is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+».

# -> greediness

import re

text = "don't tell me what to do, don't tell me what to say"

print(re.findall(r'\w+(?=n\'t)|n\'t|\w+', text))
