# class5
1. Load data
	1.1 get the name of the file
	1.2 assert if the file exists. If the file does not exist, end the program
	
2. Format the data
	2.1 look at the csv files to see how the data is divided (by spaces, commas (,), semi-columes, etc)
	2.2 check if the header exists
	2.3 split the data according to the separators and load it.
	2.4 if header does not exist, header=None
	2.5 else header= the number of rows

3. Look at it
	3.1 plot histogram
		3.1.1 import matplotlib.pyplot as plt
		3.1.2 for each column
		3.1.3	get values
		3.1.4	set the interval
		3.1.5	using plt.histo plot histogram
		3.1.6	give title for the histogram
		3.1.7	give x-label and y-label name
		3.1.8	plt.savefig(the histogram)
	3.2 plot pairs
		3.2.1 for each column
		3.2.2	get values
		3.2.3	store it in an x-axis array
		3.2.4	for each column
		3.2.5		get values
		3.2.6		store them in an y-axis array
		3.2.7	plt.scatter
		3.2.8	plt.savefig(the plot)
	3.3 plot type
		3.3.1 for each column
		3.2.2	plot type