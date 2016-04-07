
##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

##Declaring an array and intializing it to random distribution of data
#with an expected value of 100.o, s.d. of 20.0, using 10000 data points in the list
incomes = np.random.normal(100.0, 20.0, 10000)

##Plotting the histogram of the data with 50 beans
plt.hist(incomes,50)
plt.show()

##Printing the standard deviation
print incomes.std()

##Printing the variance 
print incomes.var()