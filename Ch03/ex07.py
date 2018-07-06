#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:58:22 2018

@author: vpapg
"""

import nltk

s = "A heart that's full up like a landfill \n A job that slowly kills you \n Bruises that won't heal \n You look so tired, unhappy \n Bring down the government \n They don't, they don't speak for us \n I'll take a quiet life \n A handshake of carbon monoxide"

s_list = s.split()
for element in s_list:
    nltk.re_show('^([a|A][n]?|the)$',element)


s = "107+5*4/2-9"
nltk.re_show('[\d+(\+|\-|\*|\/)?]+',s)