
# Lesson: Getting Strings from text files
"""
Text files can be read many few different ways in Python.  
Here are a few code snippets that are often useful:

# Example 1: open, read, close:
f = open("myfolder/myfile.txt", "r")  # "r" means make readable, "w" means make writeable, "rb" readable as raw bytes (data file)
text = f.read()  # gets all text by default
f.close()


# Example 2: with open, read:  
with open("myfolder/myfile.txt", "r") as f:  # automatically closes the file when the code block ends
    text = f.read()


# Example 3: Path.read_text()
from pathlib import Path
text = Path("myfolder/myfile.txt").read_text()
"""


# Exercise:  Processing the "Who's here?" list
"""
There is a file in this repo, "attendance.txt" that contains a list of people and if they are here, but it's not nicely formatted.
Read the file into python and make a dict showing whether a person is here (True or False):

attendance = {'ND': True, 'AG': True, 'BQ': False}
""" 

# Raw Data: 
import os
root_path = os.getcwd()
subdirs = r'.\data\raw'
fname = r'attendance.txt'
full_path = os.path.join(subdirs, fname)

# Script (fill in here):
# Get raw data 
with open(full_path, "r") as f:
    text = f.read()
lines = text.splitlines()

# Process data 
attendance = {}
for line in lines:
    name = line.split(' ')[0]
    if name[-1] == ':':
        name = name[:-1] 
    attendance[name] = True if '?' not in line.split(' ')[1] else False

# Output:
print(attendance)



