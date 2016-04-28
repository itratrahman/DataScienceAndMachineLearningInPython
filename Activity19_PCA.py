####This source code gives an example demonstration of Dimensionality Reduction using Principal Component Analysis

##Import Statements
import numpy as np
import pandas as pd
import matplotlib as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle

##Loading the iris datasets
iris = load_iris()

##Extracting the number of samples and number for features from the iris datasets
numSamples, numFeatures = iris.data.shape

##Print statements
print "Number of samples: ", numSamples
print "Number of features: ", numFeatures
print "Names of the iris species: ", list(iris.target_names)
print "\n"

##Extracting the feature vectors of the iris data
X = iris.data 

##Instantiating the PCA object with 2 principal components and Apply PCA on the training set 
pca = PCA(n_components = 2, whiten = True).fit(X) #whiten = True means we are going to normalize all of our data

##Extract the projected vector using the obtained PCA object
X_pca = pca.transform(X)

##Eignevectors of the chosen principal compoents; each row is a eigenvector 
print "Eignevectors of the principal compoents: ", "\n", pca.components_
print "\n"

##Printing the variance preserved in each dimension
print "Variance preserved in each dimension: ", pca.explained_variance_ratio_
print "\n"

##Print the total varaine preserved after applying PCA
print "Total Variance Preserved: ", sum(pca.explained_variance_ratio_)
print "\n"

####Plotting the 4 dimensional irish data projected down to 2 dimension

colors = cycle('rgb')

##Creating a linearly spaced list 
target_ids = range(len(iris.target_names))

pl.figure()

##For loop iterating the corresponding elements in target_ids, colors, and iris.target_names
for i, c, label in zip(target_ids, colors, iris.target_names):

	##In each iteration extract a specific equi-labelled PCA component in the all the dimensions, and plot a scatter plot from the data
	#Data with different labels are given different color codes
	#iris.target == i extract the vector of index of elements that is equal to i 
	pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1], c = c, label = label)
			 
pl.legend()
pl.show()	
	



