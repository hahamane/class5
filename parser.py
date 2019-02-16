#! usr/bin/env python
# 1. load dataset from a file
# 2. organize the text fie so we can access columns or rows of it easily
# 3. compute some summary stats about the dataset
# 4. print those summary stats


# 1. load a dataset
# 1a. import the dataset

# The reason why using argparse instead of input() is for automation
# With input(), name is required to be inputed all the time
# But with argparse, we can automate it using ls | ...

from argparse import ArgumentParser

parser = ArgumentParser(description = 'A CSV Reader + stats maker')
parser.add_argument ('csvfile', type=str,help='Path')
parsed_args=parser.parse_args()
myfile = parsed_args.csvfile
import os 
import os.path as op

# Solution 1

assert op.isfile(myfile), "give a real file"

# Solution 2
#if not op.isfile(myfile):
#	raise ValueError("not a file")

# Solution 3 (if statement to check if the file exists)

print("file is here")

# 1b load the dataset
# To install pandas:
# pip3 install --upgrade pip --user
# pip3 install pandas --user
# pip3 freeze | grep pandas to check the version of pandas
# pip3 freeze will give all the versions of packages

import pandas as pd

data = pd.read_csv(myfile, sep='\s+|,', header=None)

# If header does not have header, remove header=None

# To print the first 5 lines
print(data.head())

# Display dir items for data

# Solution 1
#for item in dir(data):
#	print(item)

# Solution 2
#print (data.shape)


# 2. Organize that file so we can access column or rows of it easily
# 2a. access any row "pandas access data by row"

# Printing all the columns between row 3 and 5 
#print (data.iloc[3:5,:])

# 2b. access any column "pandas access data by column"

# Printing the last 3 columns between row 0 to 3 
#print (data.iloc[:3,-3:])
# 2c. access any value "pandas access specific data by location"

#print (data.iloc[3,4])

# 3. Compute some summary stats of the dataset

import numpy as np

print(np.mean(data))
print(np.std(data))
