# goodFunction.py

# Demonstrates good style for returns

def absolute_value(x):
    if x < 0:
        result = -x
    else:
        result = x
    return result

### main()

y = float(input('Enter a number, or 0 to quit '))
while(y):
    z = absolute_value(y)
    print(f"{y}'s absolute value is {z}")
    y = float(input('Enter a number, or 0 to quit '))

print("Done!")
