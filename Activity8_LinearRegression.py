####This source code gives an example demonstration of Linear Regression

##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

##Creating a data set of normal distribution
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

##Creating a randomish linearly correlated data set using the normal distributed data set
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

##Plotting a scatter plot out of the created data set
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

##Training the data set with linear regression classifier
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds,purchaseAmount)

##Printing out the r value
print "R Squared value: ", r_value**2, "\n"

##Line Predictor
def predict(x):

	return slope*x+intercept

##Creating a data points for the linearly regressed line using the predictor function	
fitLine = predict(pageSpeeds)

##Comparing the data set and the linearly regressed line
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c = 'r')
plt.show()