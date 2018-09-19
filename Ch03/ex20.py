#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:28:21 2018

@author: vpapg
"""

# Write code to access a favorite webpage and extract some text from it. For example, access a weather site and extract the forecast top temperature for your town or city today.

from bs4 import BeautifulSoup
from urllib import request

url = "https://en.wikipedia.org/wiki/Radiohead"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html,"lxml").get_text()

print(raw[10021:11554])