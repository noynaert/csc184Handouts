# creates a list and prints it

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# traversing without an index
for day in days:
    print(day)
    
# traversing with an index

for i in range(len(days)):
    print(f"Day {i} is {days[i]}")
    
days[1] = "Lunes"
print("Day[1] is now ",days[1])
for day in days:
    print(day)