#Searches a word for a letter.  Return offset or -1 if not found
def find(word, letter):
  foundAt = -1 #-1 means not found yet.
  i = 0
  while foundAt == -1 and i < len(word):
      if word[i] == letter:
          foundAt = i
      i += 1
      
  return foundAt

#Searches word for a letter.  Returns true if found, otherwise false
def contains(word, letter):
    found = False
    i = 0;
    while not found and i < len(word):
        found = (word[i] == letter)
        
    return found

#Counts the number of occurrences of letter in a word. 
def count(word, letter):
    counter = 0
    
    for ch in word:
        if ch == letter:
            counter += 1
    
    return counter 
        
        
word = input("Type a word or words ")
while(len(word) == 0):
    word = input("Type a word or words (must have at least 1 character) ")
    
letter = input("Type a letter ")
while(len(letter) != 1): 
    if len(letter) != 1:
        print("Type a single character")
    letter = input("Type a letter ")

location = find(word, letter)

print(f"{letter} is at offset {location} in {word}")

