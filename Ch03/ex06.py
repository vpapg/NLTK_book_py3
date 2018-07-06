#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:44:53 2018

@author: vpapg
"""

import nltk

s = '1 day I\'m going to grow wings. A chemical reaction, hysterical and useless! Let down...'

print('(a)')
nltk.re_show('[a-zA-Z]+',s)

print('\n(b)')
nltk.re_show('[A-Z][a-z]*',s)

print('\n(c)')
nltk.re_show('p[aeiou]{,2}t','pilot poet pit paet poetry ' + s)

print('\n(d)')
nltk.re_show('\d+(\.\d+)?','12.143dsa ' +s)

print('\n(e)')
nltk.re_show('([^aeiou][aeiou][^aeiou])+',s)

print('\n(f)')
nltk.re_show('\w+|[^\w\s]+',s)