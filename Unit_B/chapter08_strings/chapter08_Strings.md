# Chapter 8, Strings

A string is a *sequence.* A sequence is a list where order matters.  It is also called an "ordered list"

Sample Strings:

* "Dog"
* 'Cat'
* '1'
* '1776'

Each item in the sequence is called an *element.*  In the case of strings, each element is a character.

### Stings may be short!

A single character is a string.

A string may have no characters.  `""` is an *empty string*


## `len(...)`

The len() function returns the number of elements in a sequence.  The length may be 0.

In a string, the len() function returns the number of characters in the string.

## Subscripts

The brackets represent a *subscript.*  The subscript represents one position in the sequence.

## Index

The value inside the brackets is called an *index.*

* The index must be a nonnegative integer
* The index uses "offset" from the beginning of the string.  
  * The first postion is [0]
  * The highest index is the length minus 1.

## Traversing a string (or sequence)

Traversing a sequence means visiting and processing every element in the sequence.  For a string this means processing every character.

### Traversal with an index

There are a couple of ways to do a traversal using an index.  This example uses a `while` loop.

* The index must be set to 0 *before* the loop begins
* The boolean expression tests for *less than* the length of the string
* The last statement must increment the index.

Style note:  i, j, and k are used for indexes.  Avoid using them for any use other than an index.

```python
word = "Happy"

i = 0
while(i < len(word)):
    print(f"The index is {i} and the letter is {word[i]}.")
    i += 1   # i = i + 1
```

### Traversal with a for statement

Sometimes we do not need the index.  We just need the elements of the sequence.

In some other languages the Python `for` loop would be called `for each` or `foreach.`  I think it makes it easier to read the loop if you read it as "for each."  So in the following code, I would read "For each ch in word"

```python
for ch in word:
    print(f"The letter is {ch}")
```

## Strings are *immutable*

Immutable means does not change.  But it looks like they can be changed.

```python
word = "Happy"
print(word)
word = "Sad"
print(word)
```

Word is actually pointing to a location in memory where the string itself is stored.

That position out in memory does not get changed.  However, the address in the variable may change.


## Searching

### Finding the first occurrence  (integer return value)

```python
# returns index of first occurrence.  Returns -1 if not found
def find(word, character):
  foundAt = -1 #-1 means not found yet.
  i = 0
  while foundAt == -1 and i < len(word):
      if word[i] == character:
          foundAt = i
      i += 1
      
  return foundAt
```

### containing (boolean return value)

```python
def contains(word, letter):
    found = False
    i = 0;
    while not found and i < len(word):
        found = (word[i] == letter)
        
    return found
```

## Counting

```python
def count(word, letter):
    counter = 0
    
    for ch in word:
        if ch == letter:
            counter += 1
    
    return counter 
```

## String methods

[https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)

### format

```python
price = 5.
priceMessage = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

## Slicing

## Examples of input validation

```python
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

```