# 02.080 Complete Program

## The file

Complete programs are stored in files.  The file must have the extension .py

```python
# fileName:  feetToMeters.py
# author: Evan Noynaert
# started: September 2021

# This program asks the user for a distance in feet.
# The program calculates the equivalent distance in meters
# The program prints the feet and the meters

# Variables
# feet    //float, The number of feet entered by the user
# meters  //float, calculated number of meters


# Get the number of feet from the keyboard
print("")  #a blank line for readability
print("How many feet? ")
feet = float(input())

# Calculate the equivalent meters
meters = feet * .3048

# Print the output
print(feet, "feet is equivalent to ", meters, "meters.")
print("") #a blank line for readability

```