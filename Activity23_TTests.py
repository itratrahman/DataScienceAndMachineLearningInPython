####This source code give a example of demonstration of dealing with outliers

##import statements
import numpy as np
from scipy import stats

np.random.seed = 2

##Creating the two randomly distributed datasets with Grp A being the test subject and Grp B being the control subject
A = np.random.normal(25.0, 5.0, 10000)
B = np.random.normal(26.0, 5.0, 10000)

##Print the the result the t-test using the pair of datasets
print stats.ttest_ind(A, B), "\n"

##Try the experiment with different sets of randomly distributed datasets
B = np.random.normal(25.0, 5.0, 10000)

##Print the the result the t-test using the pair of datasets
print stats.ttest_ind(A, B), "\n"

##Try the experiment with different sample size
A = np.random.normal(25.0, 5.0, 100000)
B = np.random.normal(25.0, 5.0, 100000)

##Print the the result the t-test using the pair of datasets
print stats.ttest_ind(A, B), "\n"

##Try the experiment with another different sample size
A = np.random.normal(25.0, 5.0, 1000000)
B = np.random.normal(25.0, 5.0, 1000000)

##Print the the result the t-test using the pair of datasets
print stats.ttest_ind(A, B), "\n"

##Running a t-test on the same datasets
print stats.ttest_ind(A, A), "\n"