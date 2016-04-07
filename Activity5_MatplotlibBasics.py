
##import statements
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

##Creating a linearly spaced vectors
x = np.arange(-3, 3, 0.001)

##Plotting a random distirbution using the vectors
plt.plot(x, norm.pdf(x))
plt.show()

##Plotting multiple plots in the same graph
plt.plot(x, norm.pdf(x), 'b-')
plt.plot(x, norm.pdf(x,1.0,0.5), 'r--')
#Setting the axis
axes = plt.axes()
axes.set_xlim([-5, 5])
axes.set_ylim([0, 1.0])
#Setting the grid
axes.grid()
#Setting the label
plt.xlabel('Greebies')
plt.ylabel('Probality')
#Setting the legend
plt.legend(['Sneeties', 'Gacks'], loc = 4)
#Saving the figure
# plt.savefig("E:\Data Science and Machine Learning in Python\Fig1.png",format = 'png')
plt.show()

####Drawing a Pie Chart
##Weghts of Pie Chart Elements
values = [12,55,4,32,14]
##Colors of Pie Chart Elements
colors = ['r', 'g', 'b', 'c', 'm']
##Labels of Pie Chart Elements
labels = ["India", "United States", "Russia", "China", "Europe"]
##Exploding out Russian segment of the pie
explode = [0, 0, 0.2, 0, 0]
##Plotting the pie chart
plt.pie(values, colors = colors, labels = labels, explode = explode)
##Setting the title
plt.title('Student Locations')
plt.show()

####Plotting a bar chart
##Weghts of Bar Chart Elements
values = [12,55,4,32,14]
##Colors of Bar Chart Elements
colors = ['r', 'g', 'b', 'c', 'm']
plt.bar(range(0,5),values , color = colors)
plt.show()

####Plotting a scatter plot
x = np.random.randn(500)
y = np.random.randn(500)
plt.scatter(x,y)
plt.show()

####Plotting a histogram
##Creating a normal distribution data set 
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()

####Plotting a Box & Whisker Plotting
uniformSkewed = np.random.rand(100)*100 -40
high_outliers = np.random.rand(10)*50+100
low_outliers = np.random.rand(10)*(-50)-100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()


