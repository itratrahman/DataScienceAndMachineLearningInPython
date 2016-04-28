####This source code gives an example demonstration of Finding Similar Movies based on Correlation of Ratings with other movies 

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
movieRatings = ratings.pivot_table(index = ['user_id'], columns = ['title'], values = 'rating')  

##Printing the head of the created table
print movieRatings.head(), "\n"

##Extracting the column for 'Star Wars (1997)'
starWarsRatings = movieRatings['Star Wars (1977)']

##Printing the head of the movie rating for star wars
print starWarsRatings.head(), "\n"

##Extracting a table of correlation between Star Wars movie rating with ratings of all other movies
#This essentially creates a correlation vector by calculating correlation of starWarsRatings vector 
#with all the columns of movieRatings matrix
similarMovies = movieRatings.corrwith(starWarsRatings)
##Dropping the NAN elements of the correlation table
similarMovies = similarMovies.dropna()
##Converting the data into panda dataframe
df = pd.DataFrame(similarMovies)
##Printing the head of the correlation table
# print df.head(10), "\n"

##Printing out the similar movies based on correlation; this is done by sorting the correlation table in descending order  
print similarMovies.order(ascending = False)

##Create a new panda data frame that aggregrates all of the rows for a given movie title
#And aggregrate specifically on the rating, we display the mean and size of the rating
movieStats = ratings.groupby('title').agg({'rating': [np.mean, np.size]})
##Printing the head of the data frame
print movieStats.head(), "\n"

##Removing movies rated by fewer than 100 people and do processing only on popular movies
popularMovies = movieStats['rating']['size'] >= 100

##Sort the popular movies among all the movies in descending order of mean rating 
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending = False)

##Creating a new data frame that joins side by side based on index (i.e. title of the movies)
#the similar movies dataframe and the data frame containing movies with more than 100 ratings
#Only the unions of the dataframes are joined, movies not found in either dataframe are discarded 
#The column of the similarMovies is given the name "similarity", this is actually the correlation columns
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns = ["similarity"]))

##Print the head of the new dataframe in the above line of code
print df.head(), "\n"

##Sort movies based on similarity values in descending order and index & display the first 15 elements
print df.sort_values(['similarity'], ascending = False)[:15], "\n"
