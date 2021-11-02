# Chapter 09 -- Files and indexing strings

A file holds data when the program is not running.

There are several ways to read files.  For now we will focus on one method

```python
#Reads a file one line at a time.

input = open('words.txt','r')

for line in input:
    line = line.strip()
    print("The line is",line)

input.close()
print("Done")
```

The above code follows a pattern for reading files tha transfers well to other languages.  This pattern is:

* Open the file
* Read the file
* Close the file

## Opening the file

Opening the file establishes a link with between the program and the file.  The file name is a string, and it may be a variable.  

```python
fileName = input("What is the name of the file? ")
file = open(fileName)
```

One important step we are skipping for now is to make sure the file exists.  It is an important step, but for right now it complicates the issue.

## Read the file

There are three basic ways to read files in Python.

1. Read one line at a time
2. Read the entire file at once as one giant string
3. Read the file as a list of strings, with each line being a separate string.

Reading one line at a time is common, especially if the file is large.  Most languages have a provision for reading a line at a time and continuing until an "End of File" is encountered.

In Python one way to read the file one line at a time is a for loop, as in the illustration.

## Close the file

When a file is open it takes up a lot of system resources.  It is best to have a file open for as short a period as possible.

The file will be closed automatically when the program ends, but it is good to get in the habit of explicitly closing files.  The file should be closed as early as possible.

Python does have some syntax that will close the file automatically, but for now we are using the more universal and easily understood method.