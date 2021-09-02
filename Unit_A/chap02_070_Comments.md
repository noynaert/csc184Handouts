# 02.070 Comments

In Python, # indicates a comment

Everything after the # to the end of the line is a comment.  This is a common convention in modern scripting languages

## Self-documenting programs

To a large extent, programs should be "self-documenting"

* Use meaningful identifiers
* Break complicated expressions into simpler and easily understood expressions
* Use functions and methods to break code into smaller and easily understood steps

## What comments to include in a program

* At the top of the program, give 
  * The name of the program (or the file name)
  * Brief description of what the program does
  * Programmer's name
  * Date.  At least the year and month it was started
* Each function should have documentation for each function
  * Brief description of what the function does
  * Restrictions on use of the function, if necessary
  * Return value, if any
  * Parameters, if any
* Data dictionaries are a good idea
* Any code that is tricky or complicated.  Hopefully, there isn't a lot of this type of code, and the code is largely self-documenting.