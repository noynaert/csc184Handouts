# exceptionExample.py
# 
# Asks for two values and calculates the quotient
# Demonstrates what happens when you divide by zero

# number -- The number to be divided (numerator of a fraction)
# divisor -- Value being divided by (denominator of a fraction)
# quotient -- The results of the division

print("Enter a number")
number = float(input())

divisor = float(input("Enter a divisor ")) #Note space after divisor
  
quotient = number / divisor

print(number,"/",quotient,"is",quotient)

print("Done!")