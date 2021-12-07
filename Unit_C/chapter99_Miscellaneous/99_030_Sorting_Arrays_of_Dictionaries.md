#  99.030 Sorting Dictionaries

## The dictionary from a file

```python
import json
import pprint

# Data is from
#https://jsonplaceholder.typicode.com/users/

fileName = "Unit_C/sampleCode/users.json"

# Opening JSON file
f = open(fileName)

# returns JSON object as
# a dictionary
users = json.load(f)

# close the file
f.close()
```

## Using a function to get the name

```python
# Gets the name field from a dictionary for a user
def getName(user):
    return user["name"]

users.sort(reverse=False, key=getName)
```

# Using a Lambda

```python
users.sort(reverse=False, key=lambda u: u["name"])
```