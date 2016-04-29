####This source code give a example of demonstration of dealing with outliers

##import statements
import numpy as np
import matplotlib.pyplot as plt

np.random.seed = 2

##Creating a normal distribution dataset with a mean value of 27000, std of 15000, using 10000 datapoints
incomes = np.random.normal(27000, 15000, 10000)

##Attaching an outlier to the dataset
incomes = np.append(incomes, [1000000000])

##Plotting the histogram of the dataset using 50 beans
plt.hist(incomes,50)
plt.show()

##Calculating the mean of the dataset
print "Mean of the dataset: ", incomes.mean(), "\n"

##Function to discard outliers that are 2 std away from the median
def reject_outliers(data):

	##Calculating the median of the dataset
	u = np.median(data)
	
	##Calculating the mean of the dataset
	s = np.mean(data)
	
	##Discard data that are 2 std away from the median
	filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
	
	return filtered
	
filtered = reject_outliers(incomes)

##Replotting the histogram of the filtered dataset using 50 beans
plt.hist(filtered,50)
plt.show()

##Calculating the mean of the filtered data
print "Mean of the dataset: ", np.mean(filtered)
