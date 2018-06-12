#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 01:00:08 2018

@author: vpapg
"""

# Review 2 on lists and strings.
#
# a. Define a string and assign it to a variable, e.g., my_string = 'My String'
# (but put something more interesting in the string).
# Print the contents of this variable in two ways, first by simply typing the 
# variable name and pressing enter, then by using the print statement.
#
# b. Try adding the string to itself using my_string + my_string, or 
# multiplying it by a number, e.g., my_string * 3. Notice that the strings are
# joined together without any spaces. How could you fix this?


print("Question (a)" + "\n")

my_string = "Colourless green ideas sleep furiously"

# 1st way (this will not work in a script)
my_string

# 2nd way (it works)
print(my_string)


print("\n"+ "\n" + "Question (b)" + "\n")

# solution with adding a whitespace
print (my_string + " " + my_string)

print()

# solution with adding a line break
print((my_string + "\n") * 3)