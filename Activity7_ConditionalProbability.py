
##import statements
import numpy as np
import matplotlib.pyplot as plt

##Setting the seed of the random class
np.random.seed(0)

##Creating a dictionary to hold population of different age groups
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}

##Creating a dictionary to hold the purchases made by different age groups
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}

##Total number of purchase
totalPurchases = 0

##For loop to iterate 100000 times
for _ in range(100000):

	##Choose randomly among a set of numbers
	ageDecade = np.random.choice([20, 30, 40, 50, 60, 70])
	
	##Calculate the probality for the age group, with the youngest age group having the lowest prob
	purchaseProbality = float(ageDecade)/100.0
	# purchaseProbality = 0.4

	##Increment the selected age group
	totals[ageDecade] += 1
	
	if (np.random.random() < purchaseProbality):
	
		totalPurchases += 1
		
		purchases[ageDecade] += 1
		
print "totals: ", totals, "\n"

print "purchases: ", purchases, "\n"

print "totalPurchases: ", totalPurchases, "\n"

##Probality of 30 year old purchasing something
PEP = float(purchases[30])/float(totals[30])
print "P(purchase | 30s): ", PEP

##Probability of being 30 year old
PF = float(totals[30])/100000
print "P(30's): ", PF

##Probability of purchasing regardless of age
PE = float(totalPurchases)/100000
print "P(purchase): ",PE

##Probility of a 30 year old purchasing:
print "P(30's)*P(Purchase): ", PE*PF

##Probability of buying sth given that the individual is in their 30s
print "P(30s, Purchase): ", float(purchases[30])/100000

##Sanity check of probality P(E|F) = P(E,F)*P(F)
print float(purchases[30])/100000/PF


	


