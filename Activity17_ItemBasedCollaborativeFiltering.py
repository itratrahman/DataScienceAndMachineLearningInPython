####This source code gives an example demonstration of Finding Similar Movies based on Item Based Collaborative Filtering 

##Import Statements
import numpy as np
import pandas as pd

##Column titles for the ratings dataset
r_cols = ['user_id', 'movie_id', 'rating']
##Reading and extracting the first 3 columns of the csv (tab limited) file from the given filepath
ratings = pd.read_csv('E:\Machine Learning in Python\DataScience\ml-100k\u.data',sep='\t', names=r_cols, usecols=range(3))

##Column titles for the movies dataset
m_cols = ['movie_id', 'title']
##Reading and extracting the first 2 columns of the csv file from the given filepath
movies = pd.read_csv('E:\Machine Learning in Python\DataScience\ml-100k\u.item', sep='|', names=m_cols, usecols=range(2))

##Merging the two datasets
ratings = pd.merge(movies, ratings)

##Printing the head i.e. first 5 rows of the dataset
print ratings.head(),"\n"

##Create a table of userid vs movies with rating values out of the dataset
userRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values = 'rating')  

##Printing the head of the created table
# print userRatings.head(), "\n"

##Calculating the correlation matrix of the table, the matrix contains correlation scores that are backed up
#by atleast 100 users rating the pair of movies considered
corrMatrix = userRatings.corr(method = 'pearson', min_periods =100)
##Printing the head of the correlation matrix
print corrMatrix.head(),"\n"

####Movie Recommendation for user id# 0

##Extracting the movie ratings for user id# 0, discarding the NAN
myRatings = userRatings.loc[0].dropna()

##Printing the user's ratings
print myRatings,"\n"

##For loop to retrieve similar movies for each movie I rated from the correlation matrix 
simCandidates = pd.Series() #Variable to store movie ratings based on the given user rating

for i in range(0,len(myRatings.index)):

	print "Adding sims for " + myRatings.index[i] + '...'
	
	##Retrieve similar movies to ith movie under consideration that the user rated 
	sims = corrMatrix[myRatings.index[i]].dropna()
	
	##Scaling the similiarity by how well the user rated the ith movie uder consideration
	sims = sims.map(lambda x: x*myRatings[i])
	
	##Adding the score to the list of similiarity candidates
	simCandidates = simCandidates.append(sims)
	
##Sorting the similarMoves dataFrame based on similarity score
simCandidates.sort_values(inplace = True, ascending = False)
##Printing the head of the dataFrame
print simCandidates.head(10), "\n"	

##The previous sorted dataFrame may have duplicated movies/entris due to movies being similar to more than one movies
#So we group the movies by the index (i.e. movie title) and sum their similarity rating
simCandidates = simCandidates.groupby(simCandidates.index).sum()

##Sorting the similarMoves dataFrame based on similarity score
simCandidates.sort_values(inplace = True, ascending = False)
##Printing the head of the dataFrame
print simCandidates.head(10), "\n"	

##Filter out the movies the user has already rated
filteredSims = simCandidates.drop(myRatings.index)
##Recommend top 10 movies based on the user ratings
print filteredSims.head(10), "\n"	