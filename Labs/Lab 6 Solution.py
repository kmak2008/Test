# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:54:30 2018

@author: Kevin
"""
import datetime
def first_days(start_year, end_year):
    date_list = []
    for i in range(start_year, end_year + 1):
        for j in range(1, 13):
            start_date = datetime.date(i, j, 1)
            date_list.append([i, start_date.strftime('%B'), 
                          start_date.strftime('%A')])
            print("Year is {0}, Month is {1}, first day is {2}".format(i, 
                  start_date.strftime('%B'), start_date.strftime('%A')))

first_days(2012, 2017)

def _removeLineEndCharacters(line):
    if line.endswith(b'\r\n'):
        return line[:-2]
    elif line.endswith(b'\n'):
        return line[:-1]
    else:
        return line
    
def fib_gen(stop):   # return Fibonacci series up to stop
    result = []
    a, b = 0, 1
    while a <= stop:
        result.append(a)
        a, b = b, a+b
    return result

print(fib_gen(100))
