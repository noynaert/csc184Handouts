# Demonstrates simple function

#combines first name and last name with a blank between
def printName(firstName, lastName):
    fullName = firstName + " " + lastName
    print(fullName)

#Adds one to a number and print it
def printIncrement(number):
    number = number + 1
    print("The number is now ",number)

first = "Ivan"
last  = "Smith"
printName(first, last)
printName("Joe", "Evans")

float(6)
float(7.0)

number = 7
printIncrement(number)
print("But back in the main program and number is",number)