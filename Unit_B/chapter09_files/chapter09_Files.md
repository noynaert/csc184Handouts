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

This reads the lines one at a time


