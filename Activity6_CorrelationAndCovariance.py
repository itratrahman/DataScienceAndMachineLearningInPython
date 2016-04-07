
##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

##function that returns the mean subtracted vector
def de_mean(x):

	xmean = np.mean(x)
	
	return [xi - xmean for xi in x]
	
##function that calculate the covariance between 2 data sets
def covariance(x,y):

	n = len(x)
	
	return np.dot(de_mean(x), de_mean(y))/(n-1)
	
##function which calculate Correlation between two data set
def correlation(x,y):

	stddevx = x.std()
	stddevy = y.std()
	
	return covariance(x,y)/stddevx/stddevy
	
##Generating a random data set
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

##Generating a random data set
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

##Plotting a scatter plot
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

##Printing out the covariance
print "Covariance: ", covariance(pageSpeeds, purchaseAmount), "\n"

##Redifining the variable purchase amount, making it dependant of pageSpeeds
purchaseAmount = np.random.normal(50.0, 10.0, 1000)/pageSpeeds

##Plotting a scatter plot of the new pair of data set
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

##Printing out the covariance
print "Covariance: ", covariance(pageSpeeds, purchaseAmount), "\n"

##Printing out the correlation
print "Correlation: ", correlation(pageSpeeds, purchaseAmount), "\n"

##Printing out the correlation using numpy built in function
print "Correlation(np): ", np.corrcoef(pageSpeeds, purchaseAmount), "\n"

##Fabricating a tolat linear relationship which is expected to give a correlation of 1
purchaseAmount = 100 - pageSpeeds*3

##Plotting a scatter plot of the new pair of data sets
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

##Printing out the correlation matrix
print "Correlation(np): ", np.corrcoef(pageSpeeds, purchaseAmount), "\n"