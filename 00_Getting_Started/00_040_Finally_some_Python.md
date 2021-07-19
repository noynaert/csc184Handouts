# 00.040  Finally some Python

Python runs in two modes.

* Interactive mode is useful for testing out code.  Interactive mode lets you type a command and have it executed immediately.
* Program mode is what we use to write programs.  We will put several commands in a file and then execute the commands in the order they occur in the file.

## Interactive mode

To run interactive mode:

1. Open a terminal window.
2. Type "python" and press enter.  (The prompt should change to >>> )
3. Type an expression, such as ```1+2```
4. Hit the enter key. (The Python interpreter executes the statement and shows the results immediately.)
   
To leave the interpreter, type ```exit()```

```
>python
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+2
3
>>> 5-3
2
>>> 99 + 5
104
>>> 3*4
12
>>> 3*4+5
17
>>> 5+3*4
17
>>> exit()
```

### Evaluate an Expression

In programming we will often hear the phrase "Evaluate an expression."  What does that mean?

An "expression" is a sequence of items that can be somehow calculated to create a value.  For example, 1+2 is an expression because it can be calculated to be 3.  

The process of calculating the value is called "evaluation."  So the fancy term "evaluate an expression" just means to calculate the corresponding value.

Expressions like 1+2 are arithmetic expressions.  There are several types of expressions we will look at later in the course.  For example, the expression 'abc'+'def' evaluates to 'abcdef'  (You may want to try that in the interpreter)

Try using the interpreter to evaluate the following expressions:

```
10 > 8
6 > 9
6 < 9
6 < 6
6 > 6
6 == 6
```

## Writing programs.

When we write an program we create a file and put commands into it.  After saving the file we run the program with they Python interpreter.

There are several things that can go wrong here.  We will work through the process of creating a program file in class.