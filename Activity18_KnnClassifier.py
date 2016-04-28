####This source code gives an example demonstration of KNN Classifer used to Predict Rating for Movies

##Import Statements
import numpy as np
import pandas as pd
from scipy import spatial
import operator

##Column titles for the ratings dataset
r_cols = ['user_id', 'movie_id', 'rating']
##Reading and extracting the first 3 columns of the csv (tab limited) file from the given filepath
ratings = pd.read_csv('E:\Machine Learning in Python\DataScience\ml-100k\u.data',sep='\t', names=r_cols, usecols=range(3))

##Printing the head of movie rating
print ratings.head(), "\n"

##Group the dataset by movie_id and aggreagrate the resulting dataframe based on rating,
# and displaying the columns for size of the rating and mean of the rating for the movies
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

##Printing the head of the dataframe
print movieProperties.head(), "\n"

##Creating a new data frame the only stores the size of the rating for each item
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
print movieNumRatings.head(), "\n"

##Normalizing the size of the rating for the data in the above dataframe
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x -np.min(x))/(np.max(x)-np.min(x)))

##Print the head of the normalized dataset created a code above
print movieNormalizedNumRatings.head(), "\n"

####Creating a dictionary to store all the genres associated with a movie, the popularity score (normalized size values), and the average rating
movieDict = {}

##Opeing and reading the data files stored in the given filepath
with open(r'E:\Machine Learning in Python\DataScience\ml-100k\u.item') as f:

	temp = ''
	
	##Iterating through each line of the data
	for line in f:
	
		##Stripping out the new line at the end and split it based on the pipe delimiters
		fields = line.rstrip('\n').split('|')
		
		##Extracting the movie id i.e. the 1st field of the data and converting it into integer
		movieID = int(fields[0])
		
		##Extract the name of the movie i.e. the 2nd field of the data
		name = fields[1]
			
		##Extract the genres info, i.e. fields 5-25 from the data	
		genres = fields[5:25]
	
		##Mapping the genres to binary int value of 0 or 1
		genres = map(int, genres)

		##Stroing the information in the dictionary: title; genres; popularity score (based on number of users rating the movies); mean rating
		movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

##Displaying the information of the 1st movieitem
print movieDict[1], "\n"

##Function to compute the spatial distance between genres of two movies and the absolute diffference between the movie's popularity score (normalized size values)
def ComputeDistance(a,b):

	##Extracting genres of the movies
	genresA = a[1]
	genresB = b[1]
	
	##Calculating the spatial distance between genres of the two movies
	genreDistance = spatial.distance.cosine(genresA, genresB)

	##Extracting the popularity score of the movies
	popularityA = a[2]
	popularityB = b[2]
	
	##Calculating the absolute difference between the popularities
	popularityDistance = abs(popularityA - popularityB)
	
	##return the sum of two distances
	return genreDistance + popularityDistance
	
##Printing out the distance between movie 2 $ movie 4
print movieDict[2], "\n"
print movieDict[4], "\n"
print ComputeDistance(movieDict[2], movieDict[4]), "\n"

####Function to extract the k nearest neighbours of a movie bases on its distance parameter above
def getNeighbors(movieID, K):

	##List to store the distance parameter described above
	distances = []
	
	##Iterating through every movie in the movie dictionary
	for movie in movieDict:
	
		##If statement to check whether movie under consideration is the movie passes as the function argument
		#if not then compute the spatial distance of the two movies 
		if (movie != movieID):
		
			##Calculate the spatial distance between the two movies based on their genres
			dist = ComputeDistance(movieDict[movieID], movieDict[movie])
	
			##Appending a tuple containing the current movie and the distance parameter to the list 
			distances.append((movie, dist))
			
	##Sorting the distances list in ascending order based on the distance parameter
	distances.sort(key = operator.itemgetter(1))
	
	##List to store the names of the nearest neighbours
	neighbors = []
	
	##For loop to extract and store the K nearest neighbours in the created list
	for x in range(K):

		#Appending the titkle of the movie to the list
		neighbors.append(distances[x][0])
		
	##Return the list to neighbours to the caller
	return neighbors
	

##Choosing the number of nearest neighbors
K = 10

##Variable to store the average rating
avgRating = 0

##Extracting the K neighbors using the above function
neighbors = getNeighbors(1,K)

##For loop to iterate through the nearest neighbors (movies) and print the title and Popularity score
for neighbor in neighbors:

	##Adding average rating of the movie to the variable
	avgRating += movieDict[neighbor][3]
	
	##Printing out the title and the popularity score of the movie under consideration
	print movieDict[neighbor][0]
	
avgRating /= float(K)

print "\n","Averaging rating of the nearest neighbors (movies): ", avgRating
