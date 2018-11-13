# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:11:09 2018

@author: Kevin
"""

 # -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:37:53 2017

@author: Kevin
"""

# Prompt for input "Your first name is: "
first_name = input("Your first name is: ")

# Prompt for input “Your last name is: “
last_name = input("Your last name is: ")

# Output “Your name is: “ and string together your 
# first and last name separated by a space.
print("Your name is: " + first_name + " " + last_name)

# OR 

print("Your name is: {0} {1}".format(first_name, last_name))

# OR
print("Your name is: {} {}".format(first_name, last_name))

# OR

print("Your name is: {first} {last}".format(
        first = first_name, 
        last = last_name))