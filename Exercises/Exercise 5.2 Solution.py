# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:10:34 2017

@author: Kevin
"""

# Write Python code to do the following:
# 1. Create while loop that adds the numbers 1 through 100
# 2. Put in a condition in the while loop that 
# if the sum at any point is divisible by 5 then exit the loop
# 3. Print the resulting sum

my_sum = 0
idx = 1
while idx < 101:
    my_sum = my_sum + idx
    print(idx)
    if my_sum % 5 == 0:
        break
    idx += 1
    
print("my_sum is: {}".format(my_sum))
