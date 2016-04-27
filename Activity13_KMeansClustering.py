####This source code gives an example demonstration of K Means Clustering

##Import Statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

##Function to create artificial income/age clusters for N people in k clusters
def createClusteredData(N,k):

	##Settting the seed of the numpy random class
	np.random.seed(10)
	
	##Variable to store the points per cluster
	pointsPerCluster = float(N)/k
	
	##Creating a list to store the training data set
	X = []
	
	##Iterating through the number of cluster
	for i in range(k):
	
		##Storing a randomly chosen value between 20000 and 200000
		incomeCentroid = np.random.uniform(20000.0, 200000.0)

		#Storing a randomly chosen value between 20 and 70
		ageCentroid = np.random.uniform(20.0, 70.0)

		##Iterating through the number of points per cluster
		for j in range(int(pointsPerCluster)): 
		
			##Appending to the list a two element list of two randomly chosen values with Gaussian Distribution probablity
			X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid,2.0)])
	
	##Coverting the list of lists to 2 dimensional numpy array		
	X = np.array(X)
		
	return X

##Create an artificial clusterd data
data = createClusteredData(100, 5)

##Plotting a scatter plot of the data set
plt.scatter(data[:,0], data[:,1])
plt.xlabel("Income")
plt.ylabel("Age")
plt.grid()
plt.show()

##Creating a K Means Clustering object with given number of clusters
k = 5
model = KMeans(n_clusters = k)

##Traing the scaled data with K Means Clustering |Function scale normalizes the data
model = model.fit(scale(data))

##Printing the cluster assingments of the data
# print model.labels_

##Creating a scatter plot of the clustered data
plt.figure(figsize = (8,6))
plt.scatter(data[:,0], data[:,1], c = model.labels_.astype(np.float))
plt.show()	