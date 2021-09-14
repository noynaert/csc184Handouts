# Chapter 02, Part 020, Strings

In Python a ***string*** is a sequence of characters surrounded by either "double quotes" or "single quotes." 

The term "single quotes" is a term used by computer programmers.  To ordinary humans it is just an apostrophe.  On most computer keyboards the "single quote" and the "double quote" are on the same key.  

```
>>> 'She sells sea shells down by the sea shore.'
'She sells sea shells down by the sea shore.'
>>> "Peter Piper picked a peck of pickled peppers."
'Peter Piper picked a peck of pickled peppers.'
```


## So what's the difference between single quotes and double quotes?

In Python there isn't much difference other than the situation where the string includes one of the quote marks.

However, note that other programming languages like Java, C, and C++ there *is* a significant difference between single and double quotes.  Also, if you are in Linux note that there is a difference between single quotes and double quotes in the BASH shell.

```
>>> "Peter Piper Picked a Peck of Pickled Peppers"
'Peter Piper Picked a Peck of Pickled Peppers'
>>> 'Rubber bumpered baby buggies'
'Rubber bumpered baby buggies'
>>> 'Mark Twain said "All generalizations are false, including this one."'
'Mark Twain said "All generalizations are false, including this one."'
>>> "We don't stop playing because we grow old; we grow old because we stop playing."
"We don't stop playing because we grow old; we grow old because we stop playing."
```

Python usually displays strings in single quotes.  So why did it display the third string in double quotes?  If you look at the third string there is an apostrophe in the word "don't"  

So we use single quotes when the string contains a double quote, and we use double quotes when the string contains a single quote.  

### The Escape character

What about the situation where the string includes both a single and double quote?  

The backslash character \ is known as the Escape character in Java and most other computer languages.  The escape character is used in situations where a character in a string might have a syntax meaning.

So a string that contains both types of quotes may use the escape character to tell Python to ignore the punctuation inside the string.

The following example has two apostrophes and two quotation marks inside the string.  The problem is solved by surrounding the entire string with double quotes and then putting \ in front of both of the apostrophes.


```
>>> 'Albert Einstein said "What counts can't always be counted; what can be counted doesn't always count."'
  File "<stdin>", line 1
    'Albert Einstein said "What counts can't always be counted; what can be counted doesn't always count."'
                                           ^
SyntaxError: invalid syntax
>>> 'Albert Einstein said "What counts can\'t always be counted; what can be counted doesn\'t always count."'
'Albert Einstein said "What counts can\'t always be counted; what can be counted doesn\'t always count."'
```

There are some other escape characters that can be handy.  Here are a couple of them

* \\ is the escape character for a backslash
* \n is used for a "new line"

However, the \n does not work as an escape character in the interactive mode.  It will work with the print() function we will cover in more detail in a later chapter. 

```
>>> 'First\nSecond\nThird'
'First\nSecond\nThird'
>>> print('First\nSecond\nThird')
First
Second
Third
```

## Another Form of a String Literal

Sometimes you may want to print a string that includes new lines, and it would be awkward to type as a single line.  This only works with the print() function.

```
>>> print('''
... There was a lady from Bright
...    whose speed was much faster than light.
... She set off one day,
...    in a relative way,
... And returned the previous night
... ''')

There was a lady from Bright
   whose speed was much faster than light.
She set off one day,
   in a relative way,
And returned the previous night
```

But what happens if the string contains special characters.  Consider the following:

```
>>> print(''' ________
... < Hello! >
...  --------
...         \   ^__^
...          \  (oo)\_______
...             (__)\       )\/\
...                 ||----w |
...                 ||     ||
... ''')
 ________
< Hello! >
 --------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/                ||----w |
                ||     ||
```

That *almost* worked.  The problem is it had a lot of special characters.  The line containing ```----W``` was not printed correctly.

The solution is to add a modifier to the string.  If there is an "r" infront of the ''' marks then the input will be treated as "raw" and escape characters will be ignored.

```
>>> print(r''' ________
... ... < Hello! >
... ...  --------
... ...         \   ^__^
... ...          \  (oo)\_______
... ...             (__)\       )\/\
... ...                 ||----w |
... ...                 ||     ||
... ... ''')
 ________
... < Hello! >
...  --------
...         \   ^__^
...          \  (oo)\_______
...             (__)\       )\/\
...                 ||----w |
...                 ||     ||
```