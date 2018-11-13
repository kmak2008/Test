# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:29:03 2018

@author: Kevin
"""

## Setting Working directory
import os
import json

## get working directory
os.getcwd()
## set working directory
path = r"D:\Development\Courseware\Topics\Introduction to Machine Learning with Python"
os.chdir(path)

# Create directory
output_path = "./Datasets/output"
if not os.path.exists(output_path):
    os.makedirs(output_path)

csv_file = output_path + "/six_cyls.csv"
json_file = output_path + "/six_cyls.json"

# if file exists, then delete it
if os.path.exists(csv_file):
    os.remove(csv_file)

if os.path.exists(json_file):
    os.remove(json_file)
    
# Read a text file
cars = open("./Datasets/mtcars.csv", "r")
six_cyls = open(csv_file, "w")
six_list = []
# Print out the results
for line in cars:
    #print(line)
    # save each line with cyl = 6 to separate file
    # split each line with a comma
    columns = line.split(sep=",")
    if columns[1] == "6":
        six_cyls.write(line)
        print(line)
        six_list.append(line)
        
# Close when done
cars.close()
six_cyls.close()

# dump JSON
with open(json_file, "w") as output_file: 
    json.dump(six_list, output_file)
    
db_file = output_path + "/lab5.db"

import sqlite3
conn = sqlite3.connect(db_file)
 
c = conn.cursor()

# Slide 4.20
# create a couple of tables with records
c.execute(''' CREATE TABLE Employee(
          ID INTEGER PRIMARY KEY ASC
          , FIRST_NAME VARCHAR(50) NOT NULL
          , LAST _NAME VARCHAR(50) NOT NULL)''')
 
c.execute("INSERT INTO Employee VALUES(1, 'Rufus', 'McGee')")
c.execute("INSERT INTO Employee VALUES(2, 'Harry', 'Potter')")
 
conn.commit()
conn.close()

# you can use shutils to remove the tree, but we didn't cover that
# shutils.rmtree(output_path)
# remove file and directory
os.remove(csv_file)
os.remove(json_file)
os.remove(db_file)
os.rmdir(output_path)

