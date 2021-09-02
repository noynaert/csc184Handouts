# 02.080 Debugging -- Types of error

## Types of Errors

* Syntax Error
* Runtime Error
* Semantic Error

### Syntax Error

* Violating the rules of Python syntax
* Generally the easiest to spot.  VS Code will probably highlight them as you type
* The interpreter will definitely catch them for you if you miss them in VS Code

### Runtime Error

* The error does not show up until the program executes
* Sometimes called "exceptions"
* Execution of the program actually stops or aborts

```
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
```
Runtime errors are more difficult to find than syntax errors, but there is no doubt that they happened!

Runtime errors make you look bad a a programmer.

### Semantic Error

A semantic error is when the program appears to function, but it does the wrong thing or returns a wrong answer.

These are the hardest to spot.  And they are the most dangerous!

Forgetting about proper order of operation would be one example of a semantic error.