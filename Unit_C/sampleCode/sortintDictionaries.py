# Sort Dictionaries in python

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

# user is a user dictionary with the field "name"
#    name MUST have a blank before the last name
# returns a reversed user name
def getReversedName(user):
    wholeName= user["name"]
    lastBlankLocation = wholeName.rfind(" ")
    lastName = wholeName[lastBlankLocation+1:]
    firstName= wholeName[:lastBlankLocation]
    reversed = lastName + ", " + firstName
    return reversed

# Demo getName
user = users[0]
print(getReversedName(user))

print("--------------------")
users.sort(reverse=False, key=getReversedName)
#pprint.pprint(users)
for user in users:
    print(getReversedName(user))
    
users.sort(reverse=False, key=lambda u: u["name"])
print("--------------------")
for user in users:
    print(user["name"])