course = {
    "id": "CSC184",
    "title": "Intro to Computer Programming",
    "creditHours": 3,
    "maxSeats": 25,
    "currentEnrollment": 14,
}

print(course)
print(type(course))
number = course["id"]
print(f"\nThe id is {number}\n")
for field in course:
    print(f"\t{field} has a value of {course[field]}")
    
for i in len(course):
    value = course[i]
    print(value)
