# 11.010 Dictionaries

```python
course = {
    "id": "CSC184",
    "title": "Intro to Computer Programming",
    "creditHours": 3,
    "maxSeats": 25,
    "currentEnrollment": 14
}
```

Sometimes we want to "bundle" a set of related values.  A Python Dictionary allows us to create a group of data that may be passed as a collection.

```python
print(course)
nextCourse = course
schedule[0] = course
```

## Type of dictionary

The command `print(type(course))` would print "dict"

## Other Terminology for Dictionaries

In other languages, Dictionaries are often called "Objects."  

* The layout of a Python Dictionary is almost identical to "JSON."  JSON is the string representation of an object in JavaScript. 
* JSON is a standard method of passing data between programs
* Most modern languages can process JSON
* Examples
  * ISS location : [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)
  * A list of recent bitcoin prices: [http://woz.cs.missouriwestern.edu/bitcoin.txt](http://woz.cs.missouriwestern.edu/bitcoin.txt)


## Key:Value pairs

Key : Value pairs are fairly common.  They consist of a string that serves as a key.  The value may be any other data type including stings, numbers, arrays, or even other dictionaries.

### Other Terminology for key:value pairs

Sometimes the key:value pair is called a "field."  This meaning is often applied when we are using a database-type of application.

Another term is "mapping."  Mapping is another term for a key:value pair.  

## Dictionary Syntax

* A dictionary is enclosed in "curly braces" or `{  }`
* Keys are in quote marks
* Every field must have a key
* If the value is a string, it must also be in quote marks
* Numeric values do not have quote marks
* Most other data types (such as dictionaries or lists) follow their normal syntax
* Commas are separators between fields
  * Note that this does not mean that fields are ended by commas.
  * In Python 3 you *may* put a comma after the last field, but I don't recommend you get in that habit.

## Accessing fields of a Dictionary

print (course["id"])

This looks like a Python List.  Except we are using a variable in place of an integer index.

```python
number = course["id"]
print(f"\nThe id is {number}\n")
for field in course:
    print(f"\t{field} has a value of {course[field]}")
```
## Length of a dictionary

The len() function returns the number of fields in a dictionary.

## Properties of a dictionary

* Dictionaries are mutable (They may be changed)
* In Python 3.7 and later, dictionaries are ordered.  In versions before 3.7 you can't count on the order.

Even though the dictionary is ordered, it cannot be iterated. 

```python
# The following code does not work
for i in len(course):
    value = course[i]
    print(value)
# The above code does not work because dictionaries are not iteratable
```