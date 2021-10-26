word = "Happy"
print(word[0])
print(word[1])
print(word[4])
#print(word[5])

pi = 3.14159
print(f"Pi is {pi:2f}")

print("Traversing the String")

i = 0
while(i < len(word)):
    print(f"The index is {i} and the letter is {word[i]}.")
    i += 1   # i++

print("-------------------")
for ch in word:
    print(f"The letter is {ch}")

print(type(word[0]))

print("Done")