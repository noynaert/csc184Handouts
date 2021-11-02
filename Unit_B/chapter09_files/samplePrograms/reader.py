#Reads files

input = open('words.txt','r')

for line in input:
    line = line.strip()
    print("The line is",line)

input.close()
print("Done")