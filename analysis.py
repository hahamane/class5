from sklearn.datasets import load_diabetes
import plotly.graph_objs as go 
import numpy as np 
import pandas as pd 
from plotly.offline import iplot, plot
import sklearn.linear_model
#Changing it to pandas
data = load_diabetes()
dataset = pd.DataFrame(data=data['data'], columns=data['feature_names'])
target = pd.DataFrame (data=data.target, columns = ['Y'])

unsortedDataset = pd.DataFrame(data=data['data'], columns=data['feature_names'])
unsortedDataset["Y"] = data.target
sortedDataset=unsortedDataset.sort_values('Y').reset_index(drop=True)

# Histogram
# Creating folder to save histograms
import os
import os.path as op 
def getRelationship():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/Relationship"
	graphs=[]
	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")

	corr = sortedDataset.corr()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
	fig.colorbar(cax)
	ticks = np.arange(0,len(sortedDataset.columns),1)
	ax.set_xticks(ticks)
	plt.xticks(rotation=90)
	ax.set_yticks(ticks)
	ax.set_xticklabels(sortedDataset.columns)
	ax.set_yticklabels(sortedDataset.columns)
	plt.savefig(str(newPath)+'/relationship.png')
	plt.clf()

def histogram():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/Histogram"

	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")
	
	for idx, column in enumerate(sortedDataset.columns):
		
		graphs=[go.Histogram(x=sortedDataset.iloc[:,idx])]
		layout = go.Layout(title=column, xaxis=dict(title=column))
		fig = go.Figure(data=graphs,layout=layout)
		plot(fig,filename="./Histogram/{0}.html".format(column),auto_open=False)
	

def pairPlot():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/PairPlot"
	graphs=[]
	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")

	graphs=[]

	for idx, column1 in enumerate(sortedDataset.columns):
		for jdx, column2 in enumerate(sortedDataset.columns):
			if (column1!=column2):
				trace = go.Scatter(
					x=sortedDataset.iloc[:,idx],
					y=sortedDataset.iloc[:,jdx],
					mode = 'markers'
				)
				title = str(column1)+" vs "+str(column2)
				layout = go.Layout(
					title=title, 
					xaxis=dict(title=column1),
					yaxis=dict(title=column2),
					showlegend=False
					)
				data=[trace]
				fig = go.Figure(data=data,layout=layout)
				plot(fig,filename="./PairPlot/{0} vs {1}.html".format(
					column1,column2),auto_open=False)	



def getAllScatter():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/MixScatterGraph"
	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")
	data = []
	for idx, column in enumerate(sortedDataset.columns):

		if (column != sortedDataset.columns[10]):
			trace=go.Scatter(
				x=sortedDataset.iloc[:,10],
				y=sortedDataset.iloc[:,idx],
				mode = 'lines+markers',
				name = column	
				)
			data.append(trace)
	title = "Attributes vs Y"
	xaxisTitle="Y"
	yaxisTitle="Attributes"
	layout = go.Layout(
				title= title, 
				xaxis=dict(title=xaxisTitle),
				yaxis=dict(title=yaxisTitle),
				showlegend=True
			)
	fig = go.Figure(data=data,layout=layout)
	plot(fig,filename="./MixScatterGraph/Attributes vs Y.html",auto_open=False)	

def getMultipleScatterWithSexAsColor():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/MultipleGraph"
	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")
	sex=sortedDataset.columns[1]
	y = sortedDataset.columns[10]
	for idx, column1 in enumerate(sortedDataset.columns):
		for jdx, column2 in enumerate(sortedDataset.columns):
			if (column1 != sex and column1 != y and column2 != sex and column2 != y and column1!=column2):
				trace = go.Scatter(
					x=sortedDataset.iloc[:,idx],
					y=sortedDataset.iloc[:,jdx],
					mode = 'markers',
					marker=dict(
						size = sortedDataset.iloc[:,10]/10,
						color = sortedDataset.iloc[:,1],
						colorbar=dict(title="Sex"),
						colorscale = 'Viridis',
						showscale = True
						)
					)
				data=[trace]
				title = column1 + " vs " + column2 + " vs Sex vs Y"
				layout = go.Layout(
				title= title, 
				xaxis=dict(title=column1),
				yaxis=dict(title=column2),
				showlegend=False
				)
				fig = go.Figure(data=data,layout=layout)
				plot(fig,filename="./MultipleGraph/{0} vs {1} vs Sex and Y.html".format(column1, column2),auto_open=False)	


def linearRegressionAnalysis():
	from sklearn.linear_model import LinearRegression
	X = dataset
	y = target["Y"]
	model = LinearRegression()
	model.fit(X,y)
	print("R2 of linear regression is " + str(model.score(X,y)))

def logarithRegressionAnalysis():
	from sklearn.linear_model import LogisticRegression
	X=dataset
	y = target["Y"]
	model = LogisticRegression()
	model.fit(X,y)
	print("R2 of Logarithmic regression is " + str(model.score(X,y)))

def RidgeAnalysis():
	from sklearn.linear_model import Ridge
	X=dataset
	y = target["Y"]
	model = Ridge(alpha=0.1)
	model.fit(X,y)
	print("R2 of Ridge regression is " + str(model.score(X,y)))

def polynomialRegressionAnalysis():
	from sklearn.preprocessing import PolynomialFeatures
	from sklearn.linear_model import LinearRegression
	X = dataset
	y = target["Y"]
	model = LinearRegression()
	poly = PolynomialFeatures(degree = 2)
	x_poly = poly.fit_transform(X)
	model.fit(x_poly, y)
	print("R2 of Polynomial regression is " + str(model.score(x_poly,y)))

#histogram()
#pairPlot()
#timeStamp()
#getAllScatter()
#getMultipleScatterWithSexAsColor()


linearRegressionAnalysis()
logarithRegressionAnalysis()
RidgeAnalysis()
polynomialRegressionAnalysis()