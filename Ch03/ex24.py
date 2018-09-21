#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 00:36:02 2018

@author: vpapg
"""

# Try to write code to convert text into hAck3r, using regular expressions and substitution, where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8. Normalize the text to lowercase before converting it. Add more substitutions of your own. Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.

import re

text = "Please could you stop the noise? I am trying to get some rest, from all these unborn chicken voices in my head..."

sub_text = re.sub('ate','8',text.lower())
sub_text = re.sub('e','3',sub_text)
sub_text = re.sub('i','1',sub_text)
sub_text = re.sub('o','0',sub_text)
sub_text = re.sub('l','|',sub_text)
sub_text = re.sub('(?<=\s)s|^s','$',sub_text)
sub_text = re.sub('s','5',sub_text)
sub_text = re.sub('\.','5w33t!',sub_text)

print(sub_text)