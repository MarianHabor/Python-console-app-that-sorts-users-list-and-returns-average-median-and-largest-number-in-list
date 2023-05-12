import statistics
import sys

# function that check if the input given by the user is numeric
def isInt(toCheck):

    if not toCheck.isnumeric():
        sys.exit('You can only input numbers')


# asking the user to input the size of the numbers they want to add
numSize = input('How many numbers you want to add? ')

# calling the function to check if the input is numeric
isInt(numSize)

# assign the user input as a int class
numSize = int(numSize)

# initialazing the list that will store every number
userNumbers = []

# iterates for n times based on the size, and ask the user
# to add a new number each time and we check if the input 
# is numberic we assign the user input as a int class
# and we append it to the list
for x in range(numSize):
    nr = input(F'Input number for {x} ')
    isInt(nr)
    nr = int(nr)
    userNumbers.append(nr)


# sorts the numbers by value
userNumbers.sort()

# prints message and the sorted numbers
print('Sorted numbers by value ', userNumbers)

# sums all values and divides them by their lenghth
average = sum(userNumbers) / len(userNumbers)

# prints message and the average
print('The average of the numbers ', average)

# to calculate the median it uses the statistics library
# and we call the median function
median = statistics.median(userNumbers)

# prints the median result
print('The median of the numbers ', median)

# we print the smallest number by accesing the index 0 of the sorted list
print('Smallest element is ', userNumbers[0])

# we print the largest number by accesing the index -1 of the sorted list
print('Largest element is ', userNumbers[-1])
