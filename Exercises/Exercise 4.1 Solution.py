# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:10:34 2017

@author: Kevin
"""
# 1. Create a list of five elements from the numbers 1 through 5
num_list = list(range(1, 6))
# OR
num_list = [1, 2, 3, 4, 5]

# 2. Create a list of five elements from the letters a through e
let_list = ['a', 'b', 'c', 'd', 'e']
# OR
let_list = list('abcde')
# OR
let_list = list(('a', 'b', 'c', 'd', 'e'))

# Optional Print the first three numbers of the first list combined with the 
# last three letters of the second list
comb_list = num_list[:3] + let_list[-3:]

# 3. Update the first three numbers of the first list to the the 
# last three letters of the second list
let_list
num_list

num_list[0:3]
let_list[2:]

num_list[0:3] = let_list[2:]
