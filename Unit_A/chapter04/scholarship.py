# Figuring out if someone is qualified for a scholarship

# Requirements for scholarship:
# Age:  Must be at least 18 
# Class: Must be a sophomore or higher
# Must live in Missouri

#Get input
age = int(input("How old are you? "))
hours = int(input("How many credit hours have you earned? "))
state = input("What state do you live in (2-letter abbreviation)? ")
state = state.upper()


#Echo Print
print("You are ", age,"years old.")
print("You have earned", hours, "credit hours")
print("You live in", state)

# Evaluate the criteria
ageTest = (age >= 18)
hoursTest = (hours >= 30)
stateTest = (state == 'MO')

print("Age Qualifies:",ageTest)
print("Hours qualify: ", hoursTest)
print("State Qualifies: ", stateTest)

#determine qualification for scholarship

scholarshipQualified = ageTest and hoursTest and stateTest
print('='*50)
print("Qualifies for scholarship:",scholarshipQualified)
print('='*50)
print()