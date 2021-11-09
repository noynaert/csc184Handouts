# reads a list of animals from a file
# note that the animals must be one per line.

def printList(array):
    print('----------------')
    for item in array:
        print(item)
    print('================')
    

fh = open("Unit_B/chapter10_Lists/sampleCode/animals.txt", 'r')

zoo =fh.readlines();


for animal in zoo:
    print(animal.strip())

printList(zoo)

for i in range(len(zoo)):
    zoo[i] = zoo[i].strip();
printList(zoo)
fh.close()

print("\nDone")