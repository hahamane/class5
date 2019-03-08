#! usr/bin/env python
# 1. load dataset from a file
# 2. organize the text file so we can access columns or rows of it easily
# 3. if the file does not have header, ask user if the user wants to add header. If yes, add
# 3. compute some summary stats about the dataset
# 4. plot histogram of a chosen column
# 5. plot scatter plot of 2 chosen column


# 1. load a dataset
# 1a. import the dataset

# The reason why using argparse instead of input() is for automation
# With input(), name is required to be inputed all the time
# But with argparse, we can automate it using ls | ...

from argparse import ArgumentParser
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import seaborn as sns

parser = ArgumentParser(description = 'A CSV Reader + stats maker')
parser.add_argument ('csvfile', type=str,help='Path')
parsed_args=parser.parse_args()
myfile = parsed_args.csvfile
import os 
import os.path as op

assert op.isfile(myfile), "give a real file"

print("file is here")

# 1b load the dataset
# To install pandas:
# pip3 install --upgrade pip --user
# pip3 install pandas --user
# pip3 freeze | grep pandas to check the version of pandas
# pip3 freeze will give all the versions of packages

import pandas as pd

data = pd.read_csv(myfile, sep='\s+|,', header=None, engine = 'python')

# Creating the folder to put the graphs
path = str(os.getcwd())
path = path+"/graph"
try:
	os.mkdir(path)
	os.mkdir(path+"/histogram")
except OSError :
	print("The folder already exists")
# Checking if the header exists
# If the first value of the table is a string, that means that 
# there is a header. Therefore, check the header, then act accordingly

checkHeader = True

try:
# If the first value is not a float, it means that there is header
	checkHeader = float(data.iloc[0,0])
# By changing the checkHeader as false we can later add the headers
	checkHeader = False

except ValueError:
	
	data = pd.read_csv(myfile, sep='\s+|,', engine = 'python')

if checkHeader == False:
	check = False

# If the user inputs wrong value, the program will keep on asking

	while check == False:
		answerHeader = input("Would you like to add header? Y/N")
		
# 3.If the answer is Yes then ask for the header

		if answerHeader =="Y" or answerHeader == "y":
			headerArray = []

# 3a. Ask for the header and store it in the headerArray arry			
			
			for i in range(0, len(data.columns)):
				header = input("What is the header for " +str(i+1)+("th column?"))	
				headerArray.append(header)

# 3b. Adding the header
			
			data = pd.read_csv(myfile, sep='\s+|,', names = headerArray, engine = 'python')
			check = True

# 3c. If the user does not want to add header, then just change check into True to exit the loop

		elif answerHeader =="N" or answerHeader == "n":
			check = True

# If the user inputs other than Y or N, then keep the check as false to rerun the question

		else:
			print("Please input correct option")

# 4. Compute some summary stats of the dataset
def getStats():
	check = True

# Ask which statistics the user wants. Using try/except, catch if the user does not
# input the required option

	while check == True:

		print("1. Averages of the columns")
		print("2. Standard Deviations of the columns")
		print("3. Exit")
		try:
			choice = int(input())

			if choice == 1:
				print("Printing averages of the columns")
				print(np.mean(data))
			elif choice == 2:
				print("Printing standard deviations of the columns")
				print(np.std(data))
			elif choice == 3:
				check = False
			else :
				print("Please choose the correct option")
		except ValueError:
			print("Please choose the correct option")

# 5. printing histogram
def getHistogram():

# 5a. Ask which column the user wants the histogram

	choice = getColumn()
# 5b. Using the result of the getColumn, plot the histogram

	fig = plt.hist(data.iloc[:,choice-1])
	
	plt.title(str(data.columns.values[choice-1]))
	plt.ylabel("Counts")
	plt.xlabel(str(data.columns.values[choice-1]))
	plt.show()
	answer = input("Do you want to save the graph? Y/N")
	if answer == "Y" or answer == "y":
		fig = plt.hist(data.iloc[:,choice-1])	
		path = str(os.getcwd())
		path = path+"/graph/histogram/"
		plt.savefig(path+str(data.columns.values[choice-1])+'.png')
	plt.clf()
# This method will return the index of the column that the user choses
def getColumn():
	
	# Printing the headers of the columns for the user to chose
	for i in range(0, len(data.columns)):
		print(str(i+1) + " " + str(data.columns.values[i]))
	check = True
	while check ==True:
		try:
			choice = int(input("which data would you like?"))
			
		except ValueError:
			print("Please choose correct option")
		if choice > len(data.columns):
			print("Please choose correct option")
		else:
			check = False
	return choice


# 6.  printing pair plot
def getPairPlot():
# 6a. Ask for the columns to be plotted.

	print("First column")
	firstChoice = getColumn()
	print("Second column")
	secondChoice = getColumn()

# 6b. Plot using the 2 columns user wants

	plt.scatter(data.iloc[:,firstChoice-1], data.iloc[:,secondChoice-1])
	plt.title(str(data.columns.values[firstChoice-1] )+ " vs " + str(data.columns.values[secondChoice-1]))
	plt.xlabel(str(data.columns.values[firstChoice-1] ))
	plt.ylabel(str(data.columns.values[secondChoice-1]))

	plt.show()

# This method will print the first 5 rows of data
def getData():
	print("Printing the data")
	print(data.head())

# This method is the menu method
def mainMenu(): 
	check = True
	while check == True:
		check = False
		print("What would you like to do?")
		print("1. View first 5 entries of data")
		print("2. View Summary stats")
		print("3. View Histogram")
		print("4. View Scatter plots of 2 columns chosen")
		print("5. Exit")

		choice = input()
		if choice == "1":
			getData()
			check = True
		elif choice == "2":
			getStats()
			check = True
		elif choice == "3":
			getHistogram()
			check = True
		elif choice == "4":
			getPairPlot()
			check = True
		elif choice == "5":
			getFourParametersGraph()
			check = True
		elif choice == "6":
			check = False
		else:
			print("Please enter valid option")
			check = True


def getFourParametersGraph():

	# 6a. Ask for the columns to be plotted.

	#print("First column")
	#firstChoice = getColumn()
	#print("Second column")
	#secondChoice = getColumn()
	#print("Third column")
	#thirdChoice = getColumn()
	#print("Fourth column")
	#fourthChoice = getColumn()

# 6b. Plot using the 2 columns user wants
	fill_color = ['#FF9999' if wt == 'red' else '#FFE888' for wt in data.iloc[:,0]]
	edge_color = ['red' if wt=='red' else 'orange' for wt in data.iloc[:,0]]
	plt.scatter(data.iloc[:,0], data.iloc[:,1], c=data.iloc[:,2], s=data.iloc[:,3])
	plt.xlabel(str(data.columns.values[0]))
	plt.ylabel(str(data.columns.values[1]))
	#sns.lmplot(data = data, x=str(data.columns.values[5-1]) , y=str(data.columns.values[6-1]), hue = str(data.columns.values[2-1]) , palette= 'Dark2', fit_reg = False, scatter_kws={"s": 20},size = str(data.columns.values[1-1]))
	clb=plt.colorbar()
	clb.ax.set_title(str(data.columns.values[2]))
	plt.show()

# Run the program
getFourParametersGraph()
