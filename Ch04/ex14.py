#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 22:51:39 2018

@author: vpapg
"""

# Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been encountered earlier.

def novel10(text):
    words = [w.lower() for w in text.split()]
    cut = int(0.9 * len(words))
    words90, words10 = words[:cut], words[cut:]
    
    print([w for w in words10 if w not in words90])

t = '''This is the place
Sit down, you’re safe now
You’ve been stuck in a lift
We’ve been trying to reach you, Thom
This is the place
It won’t hurt ever again
The smell of air conditioning
The fish are belly up
Empty all your pockets
Because it’s time to come home
This is the place
Remember me?
I’m the face you always see
You’ve been stuck in a lift
In the belly of a whale
At the bottom of the ocean
The smell of air conditioning
The fish are belly up
Empty all your pockets
Because it’s time to come home
The smell of air conditioning
The fish are belly up
Let it go
Today is the first day
Of the rest of your days
So lighten up, squirt'''

novel10(t)