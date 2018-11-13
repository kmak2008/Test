# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:32:22 2018

@author: Kevin
"""

# Input your first name into a variable
fname = input('Your first name: ')

# Input your last name into a variable
lname = input('Your last name: ')

# Create a list with your first name and last name
full_name = [fname, lname]

# Create a copy of the original list with the characters of the first and last names reversed
full_name_rev = [full_name[1], full_name[0]]

# Create a copy of the original list with the characters of the first and last names reversed
full_name_char_rev = [full_name[0][-1:-6:-1], full_name[1][-1:-8:-1]]

# Create a dictionary using the reversed characters as the value and the original names as the key
name_dict = dict(zip(full_name, full_name_char_rev))

