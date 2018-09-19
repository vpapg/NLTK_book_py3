#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 15:10:54 2018

@author: vpapg
"""

# Write a utility function that takes a URL as its argument, and returns the contents of the URL, with all HTML markup removed. Use from urllib import request and then request.urlopen('http://nltk.org/').read().decode('utf8') to access the contents of the URL.

from urllib import request
import re

def funct(url):
    raw = request.urlopen(url).read().decode('utf8')
    #print(raw.findall(r"<\<.*\>><.*><\<\>>"))
    
    print(re.sub('<[^<]+?>', '', raw))
    # https://stackoverflow.com/questions/37018475/python-remove-all-html-tags-from-string
    
funct('http://nltk.org/')
