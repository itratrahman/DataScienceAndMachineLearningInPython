
##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

####Creating a uniform distribution data set using 100000 points:
values = np.random.uniform(-10.0, 10.0, 100000)

##Plotting the histograom of the data set
plt.hist(values, 50)
plt.show()

####Plotting a Gaussian distribution function
##Creating a linearly spaced numpy array
x = np.arange(-3, 3, 0.001)
##Plotting a normal distribution using the array
plt.plot(x, norm.pdf(x))
plt.show()

####Creating a normal distribution histogram using numpy package
##Expected value of the normal distribution
mu = 5.0 
##Std of the normal distribution
sigma = 2.0
##Creating a data set form normal distribution using 10000 data points
values = np.random.normal(mu, sigma, 10000)
##Plotting the histogram
plt.hist(values, 50)
plt.show()

####Plotting Exponential PDF
##creating a linearly spaced numpy array
x = np.arange(0, 10, 0.001)
plt.plot(x, expon.pdf(x))
plt.show()

####Plotting Binomial Probality Mass Function
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, binom.pmf(x, n, p))
plt.show()

####Plotting a poisson probality mass function
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x, mu))
plt.show()
