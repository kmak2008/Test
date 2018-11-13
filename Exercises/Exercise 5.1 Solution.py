# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:10:34 2017

@author: Kevin
"""

# Write Python code to do the following:
# 1. Create a for loop the sums the numbers 1 through 10
my_sum = 0
for i in range(1, 11):
    my_sum = my_sum + i

# alternativer
my_sum = 0
my_iterator = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_iterator:
    my_sum = my_sum + i


# 2. Print the total
print('The total is {}'.format(my_sum))


    