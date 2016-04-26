####This source code gives an example demonstration of train/test split to prevent overfitting

##import statements
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.metrics import r2_score


##Creating a random normal distribution to create dataset for page speed and purchase amounts
pageSpeeds = np.random.normal(3.0, 1.0, 100) #mean value:3.0; std: 1.0; m= 100
purchaseAmounts = np.random.normal(50.0, 30.0, 100) #mean value:50.0; std:30.0; m= 100

##Plotting a scatter plot of the dataset
plt.scatter(pageSpeeds, purchaseAmounts)
#Setting the labels
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amounts")
plt.grid()
plt.show()

##Doing a test/train split on the data 
#It is recommended to do a random shuffle of the dataset, 
#we need not need to do this becuase the dataset are already randomly distributed
trainX = pageSpeeds[:80] ##The first 80 points are going to be the training set
testX = pageSpeeds[80:] ##The remaining points are going to be the test set
trainY = purchaseAmounts[:80]
testY = purchaseAmounts[80:]

##Plotting a scatter plot of the training examples
plt.scatter(trainX, trainY)
#Setting the labels
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amounts")
plt.grid()
plt.show()

##Plotting a scatter plot of the test examples
plt.scatter(testX, testY)
#Setting the labels
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amounts")
plt.grid()
plt.show()

##Converting the training set to numpy arrays
trainx = np.array(trainX)
trainy = np.array(trainY)

##Fitting an eighth degree polynomial to the dataset 
p8 = np.poly1d(np.polyfit(trainx, trainy, 8))

##Plotting the fitted polynomial and the training set
#Creating a linearly spaced array from 0 to 7 using 100 data points
xp = np.linspace(0,7,100)
#Setting the axes
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
#Setting the labels
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amounts")
#Plotting the scatter plot of training set and line plot the fitted polynomial
plt.scatter(trainx,trainy)
plt.plot(xp, p8(xp), c = 'r')
plt.show()

##Plotting the fitted polynomial and the test set
#Converting the test set to numpy arrays
testx = np.array(testX)
testy = np.array(testY)
#Setting the axes
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
#Setting the labels
plt.xlabel("Page Speeds")
plt.ylabel("Purchase Amounts")
#Plotting the scatter plot of training set and line plot the fitted polynomial
plt.scatter(testx,testy)
plt.plot(xp, p8(xp), c = 'r')
plt.grid()
plt.show()

##Calcuting the squared error of the test set
r2 = r2_score(testy, p8(testx))
print r2

##Calcuting the squared error of the training set
r2 = r2_score(trainy, p8(trainx))
print r2






