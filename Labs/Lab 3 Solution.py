# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 20:40:26 2018

@author: Kevin
"""

import math
# Prompt the user to input a number
input_num = float(input("Input a number: "))

# Output the log of that number (base 10)
print("Log base 10 of that number is: " + str(math.log10(input_num)))

log10_num = math.log10(input_num)
result = math.floor(log10_num)

# Output the nearest integer less than that number 
print("Nearest int to result is: " + str(result))

# prompt the user to input two numbers
num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
sum1 = num1 + num2
print("The sum of those two numbers is ", sum1)
