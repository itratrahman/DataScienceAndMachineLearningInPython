####This source code gives an example demonstration of Polynomial Regression

##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

##Setting the seed of the random class
np.random.seed(2)

##Creating a data set of normal distribution
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

##Creating a randomish nonlinear correlated data set using the normal distributed data set
purchaseAmount = np.random.normal(50.0, 10.0, 1000)/pageSpeeds

##Plotting a scatter plot out of the created data set
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

##Creating numpy array out the data set
x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

##Training a 4th degree polynomial to the dataset
p4 = np.poly1d(np.polyfit(x, y, 4))

##Creating a linearly spaces numpy array 
xp = np.linspace(0,7,100)
##Creating the predicted data points using the created array
yp = p4(xp)
##Plotting a scatter plot of the training set
plt.scatter(x,y)
##Plotting the predicted line 
plt.plot(xp, yp, c = 'r')
plt.show()

##Calculating the r square value
r2 = r2_score(y, p4(x))
print "R Squared Value: ", r2

