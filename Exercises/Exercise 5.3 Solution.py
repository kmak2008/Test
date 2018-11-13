# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:11:19 2018

@author: Kevin
"""

# step 1 - get input
# tests
# test 1 - can we convert this to a number from a string?
#   yes - then convert and go forward
#   no - (we will have an exception) - respond with error and continue

# test 2 - can we take the square root (is it a positive number)
#   yes - take square root, report back result and quit
#   no - (we can test or throw exception) - respond with error and continue

# continue - prompt user (go to step 1)

import math
while True:
    # Redo your square root Python code to do the following:
    # 1. Prompt for input “Enter a number: ”
    my_input = input("Enter a number: ")
    if(my_input == 'quit'):
        break
    # 2. Use an exception handler to ensure you can take the square root of the input
    # 3. If there is an exception print “Unable to calculate the square root.”
    # 4. Otherwise output “The square root of the number is: “ 
    # and provide the square root of the number.
    try:
        my_input_f = float(my_input) # if converts, nothing to do
    except ValueError:
        print("Unable to convert your input: " + my_input)
        continue
    except Exception as e:
        print("No clue: ", e)
        continue
    
    if(float(my_input) < 0):
        print("Please enter a positive number next time")
        continue
    else:
        try:
            print("The square root of the number is: {}".format(math.sqrt(my_input_f)))
            break
        except:
            print("Unable to calculate the square root of the input")
            continue

