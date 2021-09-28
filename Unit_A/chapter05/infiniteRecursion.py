# infiniteRecursion.py

# Demonstrates what happens when there is no way to stop recursion

# badCounter() is a function that counts.  It has no way to stop itself.

def badCounter(number):
    print("The count is now", number)
    next = number + 1
    badCounter(next)

# The main program starts here

print("Begin...")
badCounter(1)
print("Done!")