####This source code gives an example demonstration of Multivariate Regression

##import statements
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import r2_score

##Importing data set using pandas
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

##Printing the head of data set
print df.head()
print "\n"

##Converting the column for model names into a set of numbers 
#and inserting the column vector into the beck of the data set 
df['Model_ord'] = pd.Categorical(df.Model).codes
##Extracting the required feature vector from the imported data set 
X = df[['Mileage', 'Model_ord', 'Doors']]
##Extracting the target variables
y = df[['Price']]

##Appending a column vecotr ones to the front for the bias unit
X1 = sm.add_constant(X)
##Training created data set using a multivariate regression classifier
est = sm.OLS(y,X1).fit()

##Displaying the summary
print est.summary()

##Displaying the mean price for the given number of doors (2/4)
print y.groupby(df.Doors).mean()




