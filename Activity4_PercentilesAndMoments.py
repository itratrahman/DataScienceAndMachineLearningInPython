
##import statements
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

####Creating a normal distribution data set using 100000 points with std of 0.5:
vals = np.random.normal(0, 0.5, 100000)

##Plotting the histograom of the data set
plt.hist(vals, 50)
plt.show()

##Printing out some percentile values
print "50th percentile: ", np.percentile(vals, 50)
print "90th percentile: ", np.percentile(vals, 90)
print "20th percentile: ", np.percentile(vals, 20)

print "\n"

##Printing out the mean of the data set
print "Mean: ", np.mean(vals)

##Printing out the variance of the data set
print "Variance: ", np.var(vals)

##Printing out the skew
#Since our data set is nicely centred around 0, it should be almost 0
print "Skew: ", sp.skew(vals)

##Printing out the kurtosis of the data set
#This describes the tail, for a normal distribution this is 0
print "Kurtosis: ", sp.kurtosis(vals)




