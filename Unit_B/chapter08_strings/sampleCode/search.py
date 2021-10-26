#Searches a word for a character.  Return offset or -1 if not found
def find(word, character):
  foundAt = -1 #-1 means not found yet.
  i = 0
  while foundAt == -1 and i < len(word):
      if word[i] == character:
          foundAt = i
      i += 1
      
  return foundAt

#Searches word for a character.  Returns true if found, otherwise false
def contains(word, character):
    found = False
    i = 0;
    while not found and i < len(word):
        found = (word[i] == character)
        
    return found

#Counts the number of occurrences of character in a word. 
def count(word, character):
    counter = 0
    
    for ch in word:
        if ch == character:
            counter += 1
    
    return counter 
        
# gets a word of length > 0
def getWord():        
    word = input("Type a word or words ")
    while(len(word) == 0):
        word = input("Type a word or words (must have at least 1 character) ")
    return word

# gets a single character or
def getCharacter():    
    character = input("Type a character ")
    while(len(character) != 1): 
        if len(character) != 1:
            print("Type a single character")
        character = input("Type a character ")
    return character

# returns a letter of the English alphabet
def getLetter():
    letter = input("Type a letter ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len!=1 and not contains(alphabet, letter.lower()):
            letter = input("Type a letter of the English alphabet ")

    return letter


word = getWord()
character = getCharacter()

location = find(word, character)

print(f"{character} is at offset {location} in {word}")

