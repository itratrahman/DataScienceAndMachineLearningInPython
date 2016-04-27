####This source code gives an example demonstration of Decision Tree Classifier and Random Forest Classifier

##Import Statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
# from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn.ensemble import RandomForestClassifier
import pydot

##Input filepath
pilepath = "E:\Introduction to Machine Learning\PastHires.csv"

##Reading CSV file from the file path 
df = pd.read_csv(pilepath, header = 0)

#Printing the head i.e top 5 lines of the dataset
print df.head(), "\n"

####Scikit Learn requires everything to be numerical.
#So we have to map Y,N to 1,0 and education to some scale of 0-2

##Mapping the Y & N of "Employed", "Hired", "Top Tier Schools" columns to 0 & 1 
d = {'Y':1, 'N':0} #Mapping dictionary which maps Y & N to 1 & 0
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2} #Mapping dictionary which maps 'BS', 'MS', 'PhD' to 0,1,2
df['Level of Education'] = df['Level of Education'].map(d)

##Printing the updated dataset after relevant mapping
print df.head(),"\n"

##Creating the list of feature names
features = list(df.columns[:6])

#Print features
print features,"\n"

##Extracting the feature vector from the dataset
X = df[features]
##Extracting the target variables from the dataset
Y = df["Hired"]

##Instantiating a decision tree classifier object
classifier = tree.DecisionTreeClassifier()

##Training the classifier using the data set
model = classifier.fit(X,Y)

####Creating a graph of the decios
# dot_data = StringIO()
# tree.export_graphviz(model, out_file=dot_data, feature_names=features)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png()

##Predicting for 2 set of data
print model.predict([[10, 1, 4, 0, 0, 0]])
print model.predict([[10, 0, 4, 0, 0, 0]])
print "\n"

####Testing the traing set with Random Forest Classifier
estimators = 10 #Number of estimators for Random Forest Classifier

##Instantiating a random forest classifier object
classifier = RandomForestClassifier(n_estimators = estimators)

##Training the classifier using the data set
model = classifier.fit(X,Y)

##Predicting for 2 set of data
print model.predict([[10, 1, 4, 0, 0, 0]])
print model.predict([[10, 0, 4, 0, 0, 0]]) 