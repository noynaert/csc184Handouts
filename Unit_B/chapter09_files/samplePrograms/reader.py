#Reads files

#input = open('words.txt','r')
input = open('http://woz.cs.missouriwestern.edu/data/docs/moby.txt')

for line in input:
    line = line.strip()
    print("The line is",line)

input.close()
print("Done")