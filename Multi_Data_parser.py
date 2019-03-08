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
import matplotlib
from matplotlib.figure import Figure
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go 
import pandas as pd
import os 
import os.path as op

parser = ArgumentParser(description = 'A CSV Reader + stats maker')
parser.add_argument ('csvfile', type=str,help='Path')
parsed_args=parser.parse_args()
myfile = parsed_args.csvfile
assert op.isfile(myfile), "give a real file"
path = str(os.getcwd())
newPath = path+"/"+os.path.splitext(myfile)[0]
try:
	os.mkdir(newPath)
except OSError as e:
	print("Already exists")
# 1b load the dataset
# To install pandas:
# pip3 install --upgrade pip --user
# pip3 install pandas --user
# pip3 freeze | grep pandas to check the version of pandas
# pip3 freeze will give all the versions of packages



data = pd.read_csv(myfile, sep='\s+|,', header=None, engine = 'python')

# Checking if the header exists
# If the first value of the table is a string, that means that 
# there is a header. Therefore, check the header, then act accordingly
headerFile = None
try:
# If the first value is not a float, it means that there is header
	checkHeader = float(data.iloc[0,0])
	headerFile = path+"/header/"+str(myfile)

except ValueError:
	
	data = pd.read_csv(myfile, sep='\s+|,', engine = 'python')

# Adding the headers that I have created in the header folder
headerArray=[]
if headerFile is not None:
	try:
		os.path.isfile(headerFile)

	except Exception as e:
		print("File does not exists")

	with open(headerFile, 'r') as file_handle:
		for line in file_handle.readlines():
			values = line.split(';')
			for value in values:
				headerArray.append(str(value))

	data = pd.read_csv(myfile, sep='\s+|,', names = headerArray, engine = 'python')


# 4. Compute some summary stats of the dataset
def getStats(newPath):
	fileName = newPath + "/Stats/stats.txt"
	try:
		os.mkdir(newPath+"/Stats")
		
	except OSError as e:
		print("Already exists")
	f = open(fileName, "w")
	f.write("mean\n")
	
	for idx, item in enumerate(np.mean(data,axis=0)):
		f.write(str(data.columns.values[idx])+": "+str(item)+"\n")
	
	f.write("Standard Deviation\n")
	for idx, item in enumerate(np.std(data,axis=0)):
		f.write(str(data.columns.values[idx])+": "+str(item)+"\n")
	
	#np.save(f, average)
	#f.write("Standard Deviation")
	#np.save(f, np.std(data,axis=0))
	
	



# 5. printing histogram
def getHistogram(path):
	newPath = path+"/Histogram" 
	try:
		os.mkdir(newPath)
		
	except OSError as e:
		print("Already exists")

	for idx, column in enumerate(data.columns):
		fig = plt.hist(data.iloc[:,idx])
		plt.savefig(str(newPath)+"/"+str(column)+'.png')
		plt.title(str(column))
		plt.ylabel("Counts")
		plt.xlabel(str(column))
		plt.clf()



# 6.  printing pair plot
def getPairPlot(path):
# 6a. Ask for the columns to be plotted.
	newPath = path+"/Scatter_Plot" 
	try:
		os.mkdir(newPath)
		
	except OSError as e:
		print("Already exists")
	for idx, column1 in enumerate(data.columns):
		for jdx, column2 in enumerate(data.columns[idx+1:]):
			plt.title(str(column1)+ " vs " + str(column2))
			plt.xlabel(str(column1))
			plt.ylabel(str(column2))
			fig = plt.scatter(data.iloc[:,idx], data.iloc[:,jdx])
			plt.savefig(str(newPath)+"/"+str(column1)+"_"+str(column2)+'.png')
			plt.clf()

def getRelationPlot(path):
	newPath = path+"/Relationship" 
	try:
		os.mkdir(newPath)
		
	except OSError as e:
		print("Already exists")
	corr = data.corr()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
	fig.colorbar(cax)
	ticks = np.arange(0,len(data.columns),1)
	ax.set_xticks(ticks)
	plt.xticks(rotation=90)
	ax.set_yticks(ticks)
	ax.set_xticklabels(data.columns)
	ax.set_yticklabels(data.columns)
	plt.savefig(str(newPath)+'/relationship.png')
	plt.clf()
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
def get4DPlot(path):
	newPath = path+"/4D_Plots"
	try:
		os.mkdir(newPath)
		
	except OSError as e:
		print("Already exists")

#	print("First column")
#	firstChoice = getColumn()
#	print("Second column")
#	secondChoice = getColumn()
#	print("Third column")
#	thirdChoice = getColumn()
#	print("Fourth column")
#	fourthChoice = getColumn()

# 6b. Plot using the 2 columns user wants
	#plt.scatter(data.iloc[:,firstChoice-1], data.iloc[:,secondChoice-1], c=data.iloc[:,thirdChoice-1], s=data.iloc[:,fourthChoice-1])
	#plt.xlabel(str(data.columns.values[firstChoice-1]))
	#plt.ylabel(str(data.columns.values[secondChoice-1]))
	#clb=plt.colorbar()
	#clb.ax.set_title(str(data.columns.values[thirdChoice-1]))
	#plt.savefig(str(newPath)+"/"+str(data.columns.values[firstChoice-1] )+"_"+str(data.columns.values[secondChoice-1] )+"_"+str(data.columns.values[thirdChoice-1] )+"_"+str(data.columns.values[fourthChoice-1] )+'.png')
	#plt.clf()
	for column1 in data.columns[1:]:
		for column2 in data.columns[2:]:
			#for column3 in data.columns[3:]:
					data1 = data[column1]
					data2 = data[column2]
					#data3 = data[column3]
					plt.scatter(data1, data2, c=data.iloc[:,1], s=data.iloc[:,0], cmap='viridis')
					plt.xlabel(str(column1))
					plt.ylabel(str(column2))
					clb=plt.colorbar()
					clb.ax.set_title("Sex")
					plt.title(column1 + "vs"+column2 + "vs"+"Sex" + "vs AGE")
					plt.savefig(str(newPath)+"/"+str(column1)+"_"+str(column2)+"_Sex_AGE.png")
					plt.clf()
					
getStats(newPath)
getHistogram(newPath)
getPairPlot(newPath)
getRelationPlot(newPath)
get4DPlot(newPath)