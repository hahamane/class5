from sklearn.datasets import load_diabetes
import plotly.graph_objs as go 
import numpy as np 
import pandas as pd 
from plotly.offline import iplot, plot
import matplotlib.pyplot as plt

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

def getMultipleScatter():
	currentPath = str(os.getcwd())
	newPath = currentPath + "/MultipleGraph"
	try:
		os.mkdir(newPath)
	except OSError:
		print ("The folder already exists")
	
	y = sortedDataset.columns[5]
	for idx, column1 in enumerate(sortedDataset.columns):
		for jdx, column2 in enumerate(sortedDataset.columns):
			if (column1 != y and column2 != y and column1!=column2):
				trace = go.Scatter(
					x=sortedDataset.iloc[:,idx],
					y=sortedDataset.iloc[:,jdx],
					mode = 'markers',
					marker=dict(
						size = sortedDataset.iloc[:,5]/10

## If you want to play with colors, please adjust following code

						#color = sortedDataset.iloc[:,5],
						#colorbar=dict(title="Y"),
						#colorscale = 'Viridis',
						#showscale = True
						)
					)
				data=[trace]
				title = column1 + " vs " + column2 + " vs Y"
				layout = go.Layout(
				title= title, 
				xaxis=dict(title=column1),
				yaxis=dict(title=column2),
				showlegend=False
				)
				fig = go.Figure(data=data,layout=layout)
				plot(fig,filename="./MultipleGraph/{0}_vs_{1}_vs_Y.html".format(column1, column2),auto_open=False)	

def leastSquareAnalysis():
	import statsmodels.api as sm 
	dataset.drop('age', axis = 1, inplace =True)
	dataset.drop('s2', axis = 1, inplace =True)
	dataset.drop('s3', axis = 1, inplace =True)
	dataset.drop('s4', axis = 1, inplace =True)
	dataset.drop('s6', axis = 1, inplace =True)
	X2 = sm.add_constant(dataset)
	est = sm.OLS(target,X2)
	est2 = est.fit()
	print(est2.summary())	

def modelSelection():
	from sklearn.model_selection import KFold
	from sklearn import model_selection
	from sklearn.linear_model import LinearRegression
	from sklearn.linear_model import Ridge
	from sklearn.preprocessing import PolynomialFeatures
	
	dataset.drop('age', axis = 1, inplace =True)
	dataset.drop('s2', axis = 1, inplace =True)
	dataset.drop('s3', axis = 1, inplace =True)
	dataset.drop('s4', axis = 1, inplace =True)
	dataset.drop('s6', axis = 1, inplace =True)
	
	seed = 7
	kf = KFold(n_splits=10, random_state=seed)
	linearModel = LinearRegression()
	results = model_selection.cross_val_score(linearModel,dataset,target,cv=kf)
	print("Accuracy for linear regression : %3.f%%(%.3f%%)" % (results.mean()*100.0, results.std()*100.0) )

	ridgeModel = Ridge()
	results = model_selection.cross_val_score(ridgeModel,dataset,target,cv=kf)
	print("Accuracy for Ridge : %3.f%%(%.3f%%)" % (results.mean()*100.0, results.std()*100.0) )

	poly = PolynomialFeatures(degree = 2)
	X = poly.fit_transform(dataset)
	polynomialModel = LinearRegression()
	results = model_selection.cross_val_score(polynomialModel,X,target,cv=kf)
	print("Accuracy for polynomial regression : %3.f%%(%.3f%%)" % (results.mean()*100.0, results.std()*100.0) )


#histogram()
#pairPlot()
#getAllScatter()
#getMultipleScatter()
#getRelationship
#modelSelection()
leastSquareAnalysis()
