# Simple boolean variables

peopleHome = 0
lightsOn = False

peopleHome = int(input("How many people are home? "))
print("People home is", peopleHome)

lightsOn = (peopleHome > 0)
print("Lights on:", lightsOn)