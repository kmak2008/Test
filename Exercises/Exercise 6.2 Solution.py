# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:10:34 2017

@author: Kevin
"""
# 1. Create a list of five elements from the numbers 1 through 5
my_list = list(range(1, 6))

# 2. Create a function to take a list and a value and 
# multiply each element of the list by the value, 
# then return the resulting list
def mult_by_value(a_list, a_value):
    result = [x * a_value for x in a_list]
    return result

# 3. Try your function with your list and the value 10. 
new_list = mult_by_value(my_list, 10)
#  Print the result.
print(new_list)
