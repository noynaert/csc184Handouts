# readFile.py

import json

fileName = "person.json"

# Opening JSON file
f = open(fileName)

# returns JSON object as
# a dictionary
person = json.load(f)

# close the file
f.close()

print(person)
