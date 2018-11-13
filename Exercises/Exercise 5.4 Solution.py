# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:13:55 2018

@author: Kevin
"""

# 1. Create a list of five elements from the numbers 1 through 5
my_list = list(range(1, 6))

# 2. Use comprehension to multiple each element by 3
[i * 3 for i in my_list]