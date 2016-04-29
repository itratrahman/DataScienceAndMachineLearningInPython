####This source code gives an example demonstration of K-fold Cross Validation to avoid Over-fitting

##Import Statements
import numpy as np
import matplotlib as plt
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.datasets import load_iris

##Loading the iris datasets
iris = load_iris()

##Splitting the dataset into train and test set, with test test/train ratio of 0.4%
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(iris.data, iris.target, test_size = 0.4, random_state = 0)

####Measuring accuracy of SVM classifier with linear kernel

##Instantiating a SVM classifier object and traning the classifier with the training set
clf = svm.SVC(kernel = 'linear', C = 1).fit(X_train, Y_train)

##Accuracy score of the classifier of single train-test split
print "Accuracy Socre of single train test split: ", clf.score(X_test,Y_test), "\n"

##Using scikit learn cross_val_score to retreive the accuracy scores of 5 fold cross validation
scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv= 5)

##Print the accuracy of each fold
print "Accuracy of each fold: ", scores, "\n"

##Print the mean of accuracy of all 5 folds
print "Mean of accuracy of all folds: ", scores.mean(), "\n"

####Measuring accuracy of SVM classifier with polynomial kernel

##Instantiating a SVM classifier object and traning the classifier with the training set
clf = svm.SVC(kernel = 'poly', C = 1).fit(X_train, Y_train)

##Using scikit learn cross_val_score to retreive the accuracy scores of 5 fold cross validation
scores = cross_validation.cross_val_score(clf, iris.data, iris.target, cv= 5)

##Print the accuracy of each fold
print "Accuracy of each fold: ", scores, "\n"

##Print the mean of accuracy of all 5 folds
print "Mean of accuracy of all folds: ", scores.mean(), "\n"

##Accuracy score of the classifier of single train-test split
print "Accuracy Socre of single train test split: ", clf.score(X_test,Y_test), "\n"
