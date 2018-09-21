#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 23:07:45 2018

@author: vpapg
"""

# Examine the results of processing the URL http://news.bbc.co.uk/ using the regular expressions suggested above. You will see that there is still a fair amount of non-textual data there, particularly Javascript commands. You may also find that sentence breaks have not been properly preserved. Define further regular expressions that improve the extraction of text from this web page.

from bs4 import BeautifulSoup
from urllib import request
import re

url = "http://news.bbc.co.uk/"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html,"lxml").get_text()

print('1',len(raw))
raw = re.sub(r'var.+;','', raw)
print('2',len(raw))
raw = re.sub(r'_.+;','', raw)
print('3',len(raw))
raw = re.sub(r'(\{.+)+;','', raw)
print('4',len(raw))
raw = re.sub(r'\/\*.+\*\/','', raw)
print('5',len(raw))
raw = re.sub(r'function.+\(.*\) \{.+\}', '' ,raw)
print('6',len(raw))
raw = re.sub(r'<.+>', '', raw)
print('7',len(raw))
raw = re.sub(r'[a-zA-Z]+\.[a-zA-Z]+', '', raw)
print('8',len(raw))
raw = re.sub(r'if.+\(.+\).+\{.+\}', '', raw)
print('9',len(raw))
raw = re.sub(r'\(\);', '', raw)
print('10',len(raw))
#raw = re.sub(r'(\()?function.*\(\)\{.+\);', '', raw)
#print('11',len(raw))
#raw = re.sub(r'\} else \{.+/}', '', raw)
#print('12',len(raw))

print(raw)