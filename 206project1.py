import os
import csv
import operator
import filecmp
from datetime import date

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.
	readingFile = csv.DictReader(open(file))
	dlist = []
	for row in readingFile:
		dlist.append(row)
	return dlist
	

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	Information = sorted(data, key = operator.itemgetter(col))
	word = Information[0]['First'] + ' ' + Information[0]['Last']
	return word

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	numFreshman = 0
	numSophomores = 0
	numJuniors = 0
	numSeniors = 0
	for items in data:
		if(items['Class'] == 'Freshman'):
			numFreshman +=1
		if(items['Class'] == 'Sophomore'):
			numSophomores +=1
		if(items['Class'] == 'Junior'):
			numJuniors +=1
		if(items['Class'] == 'Senior'):
			numSeniors +=1
	newList = []
	one = ('Freshman', numFreshman)
	newList.append(one)
	two = ('Sophomore', numSophomores)
	newList.append(two)
	three = ('Junior', numJuniors)
	newList.append(three)
	four = ('Senior', numSeniors)
	newList	.append(four)
	finalList = sorted(newList, key=operator.itemgetter(1), reverse = True)
	return finalList




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	dictionary = {}
	for x in a:
		age = x['DOB']
		dates = age.split("/")
		day = dates[1]
		if day not in dictionary:
			dictionary[day] = 1
		else:
			dictionary[day] += 1
	return int(max(dictionary,key = dictionary.get))


 


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer. You will need to work with the DOB to find their current age.
	import math		
	today = str(date.today())
	today = today.split('-')
	dateYear = today[0]
	dateMonth = today[1]
	dateDay = today[2]
	numPeople = 0
	totalAge = 0
	for x in a:
		age = x['DOB']
		dates = age.split("/")
		month = dates[0]
		day = dates[1]
		year = dates[2]
		currentAge = int(dateYear) - int(year)
		if(dateMonth < month):
			currentAge -= 1
		numPeople+=1
		totalAge +=currentAge
	averageAge = int(totalAge) /  int(numPeople)
	averageAge = math.ceil(averageAge)
	return averageAge


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	
	Information = sorted(a, key = lambda x: x[col])
	openedFile = open(fileName, 'w')
	for items in Information:
		openedFile.write('{},{},{}\n'.format(items['First'], items['Last'], items['Email']))
	openedFile.close()
	



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

