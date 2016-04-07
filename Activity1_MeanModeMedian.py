
##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

##Declaring an array and intializing it to random distribution of data
#with an expected value of 27000, s.d. of 15000, using 10000 data points in the list
incomes = np.random.normal(27000, 15000, 10000)

##Printing the mean of the data
print np.mean(incomes)

##Plotting the histogram of the data with 50 beans
plt.hist(incomes,50)
plt.show()

##Printing the median
print np.median(incomes)

##Adding an outlier
incomes = np.append(incomes, [1000000000])

##Printing the mean of the data || we will notice a significant change in mean due to outlier
#The mean is skewed by one big outlier
print np.mean(incomes)

##Printing the median
print np.median(incomes)

##Generate random integers with los value of 18, and high value of 90
ages = np.random.randint(18, high = 90, size = 500)

print ages

##Print the mode of the data set
#Formal of the return value: mode, frequency
print stats.mode(ages)