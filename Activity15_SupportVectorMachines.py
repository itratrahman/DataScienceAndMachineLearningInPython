####This source code gives an example demonstration of Support Vector Machines

##Import Statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets


##Function to create artificial income/age labelled clusters 
def createClusteredData(N,k):

	##Settting the seed of the numpy random class
	np.random.seed(10)
	
	##Variable to store the points per cluster
	pointsPerCluster = float(N)/k
	
	##Creating a list to store the feature vector of the training data set
	X = []
	##Creating a list to store the target varaibles of the training data set
	Y = []
	
	##Iterating through the number of cluster
	for i in range(k):
	
		##Storing a randomly chosen value between 20000 and 200000
		incomeCentroid = np.random.uniform(20000.0, 200000.0)

		#Storing a randomly chosen value between 20 and 70
		ageCentroid = np.random.uniform(20.0, 70.0)

		##Iterating through the number of points per cluster
		for j in range(int(pointsPerCluster)): 
		
			##Appending to the list a two element list of two randomly chosen values with Gaussian Distribution probability
			X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid,2.0)])
	
			##Apeending the current label to the target variable yield
			Y.append(i)
			
	##Coverting the lists to numpy arrays		
	X = np.array(X)
	Y = np.array(Y)
		
	return X, Y

##Create a labelled artificial data set
[X, Y] = createClusteredData(100, 5)

##Plotting a scatter plot of the labelled data set
plt.scatter(X[:,0], X[:,1], c = Y.astype(np.float))
plt.xlabel("Income")
plt.ylabel("Age")
plt.grid()
plt.show()

##Instantiating a SVM classifier object
C = 1.0 #Setting the SVM regularization term
svc = svm.SVC(kernel = 'linear', C = C).fit(X,Y)

##A fucntion to plot the labelled dataset and the meshgrid to show the zones of different classes of the SVM classifier
def plotPredictions(clf):

	##Creating a meshgrid by passing the following linearly spaced numpy array
	xx, yy = np.meshgrid(np.arange(0, 250000, 10),np.arange(10, 73, 0.5))
	
	##Unrolling the meshgrid xx and yy matrices into two vectors, which are then concatenated side by side 
	#to form all combination of pairs of data x and y in the meshgrid
	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
	
	plt.figure(figsize=(8, 6))
	
	##Reshaping the matice of two columns into the shape of the created meshgrid above
	Z = Z.reshape(xx.shape)
	
	##Plotting the contour plot of the meshgrid with Z/magnitude values
	plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=1.0)
	
	##Plotting the scatter plot of the labelled data set
	plt.scatter(X[:,0], X[:,1], c=Y.astype(np.float))
	
	plt.show()

##Plotting plot the labelled dataset and the meshgrid to the zones of different classes of the SVM classifier
plotPredictions(svc)