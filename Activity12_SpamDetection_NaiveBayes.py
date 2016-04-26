####This source code gives an example demonstration of Spam Detection using Naive Bayes Classifier

import os
import io
import numpy
import pandas as pd
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

####Fucntion to read files from the given data path
def readFiles(path):

	for root, dirnames, filenames in os.walk(path):
	
		for filename in filenames:
			
			path = os.path.join(root, filename)
			
			inBody = False
			
			lines = []
			
			f = io.open(path, 'r', encoding='latin1')
			
			for line in f:
			
				if inBody:
				
					lines.append(line)
					
				elif line == '\n':

					inBody = True

			f.close()
			message = '\n'.join(lines)

			yield path, message
	
##Function to create a panda dataframe from a directory path 	
def dataFrameFromDirectory(path, classification):
        
		##Creating the list to store the data content set of the panda data frame
		rows = []
        
		##Creating the list to store the index column of the panda data frame
		index = []
        
		##Iterating through each file in the path and formatting the data using the readFiles method
		for filename, message in readFiles(path):
        
			##Appending the data content i.e. the "message" and "class" of each email, 
			#to a list which will act as the content of the dataframe
			rows.append({'message': message, 'class': classification})

			##Appening the file name to the list which will act as the index of the panda dataframe
			index.append(filename)
			
		##return a panda DataFrame containing rows for messages and classes and the row of index
		return pd.DataFrame(rows, index=index)
			
			
##Creating a panda dateframe of two columns, one to contain the messages, and one to contain the class, of the emails	
#The dataframe contains two elements of empty lists		
data = pd.DataFrame({'message': [], 'class': []})

##Appending the message and class info of all the spam emails to the dataframe 
data = data.append(dataFrameFromDirectory('E:/Machine Learning in Python/DataScience/emails/spam', 'spam'))

##Appending the message and class info of all the non spam emails to the dataframe 
data = data.append(dataFrameFromDirectory('E:/Machine Learning in Python\DataScience/emails/ham', 'ham'))

##Printing the head of the data, which displays the top 5 rows of the data set
print data.head()

##Count Vectorizer convert a collection of text documents to a matrix of token counts
#Instantiating a count vectorizer object
vectorizer = CountVectorizer()
#Extracting the matrix of token which act as the feature vector for the classifier
counts = vectorizer.fit_transform(data['message'].values)

##Extracting the target variables
targetVariables = data['class'].values

##Instantiating the multinomial Naive Bayes classifier object
classifier = MultinomialNB()

##Training the classifier using the dataset
classifier.fit(counts, targetVariables)

##Creating an test two examples and storing them in a list of string
examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]

##Executing count vectorizer method on the test examples
example_counts = vectorizer.transform(examples)

##Creating a predicticetion matrix using classifer on the list of test examples
predictions = classifier.predict(example_counts)

##Print the prediction matrix
print predictions



