 # -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:37:53 2017

@author: Kevin
"""

from datetime import date, datetime
# Convert your birthday to a date
my_birthday = datetime.strptime("1990/08/21","%Y/%m/%d")

# Print the date your were born
print("I was born on " + my_birthday.strftime("%m %d %Y"))

# better
print("I was born on " + my_birthday.strftime("%A, %B %d, %Y"))

# Print the weekday you were born - this is easy
print("I was born on a " + my_birthday.strftime("%A"))

