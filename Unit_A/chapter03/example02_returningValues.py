# Example of function that return a value

#doubles the parameter
def double(number):
    result = number + number
    return number

# The following doesn't do anything effective
double(5)
double(6.0)
double("hello")

print( double(5) )
print( double(6.0) ) 
print( double("hello"))

big = double(6)
print(big)
