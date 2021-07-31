# Chapter 02.030, Variables and Assignment Statements

***Warning*** A lot of things in this unit resemble rules and terms that are taught in Math courses.  But be very, very careful because sometimes Python syntax and math appear to be in conflict.

For example, consider the following simple statement.

    x = x + 1

The above statement is a good statement in Python.  In fact we use these types of statements frequently.

But the statement is not valid algebra.  There is no value for x that will make the equation true.  

## Variables

A variable is a place to store a number, string, or other value.

Consider the following example.

```
>>> x = 5
>>> message = "Hello"
>>> x
5
>>> message
'Hello'
```

The first statement, ```x = 5``` causes the numeric value 5 in the variable x.  After that x may be used to represent the current value stored in x.

The second statement ```message = Hello``` stores a string in the variable message.  

The value stored in a variable may change.  For example:

```
>>> minimum = 5.4
>>> minimum = 5.2
>>> minimum
5.2
```

In immediate mode it is pretty clear that assignments occur sequentially starting at the top.  In programs we typically do more looping, conditional statements, and function calls.  Figuring out the current value can be tricky and used to always requir tracing through the logic of the code.  Code tracing is still an important skill, but modern programmers can also take advantage of debuggers that can help trace the logic.  We will cover the use of debuggers later, but it is still important to be able to trace code by hand.


## Assignment Statements

An assignment statement assigns a value to a variable.  ```x = 5``` is an example.

### About the "Replacement Operator"

In Python the = symbol is called the "replacement symbol."  

My strong recommendation is to avoid calling the = symbol as "equals."  

When you are reading an assignment statement like "x = 5" should be read as "x *takes on the value of* 5."  Do not read it as "x equals 5"

### Order Matters

In Math it doesn't really matter what is on the left side of  the = symbol.  For example, the following are equivalent in mathematics.

```
x = 5
5 = x
```

In math

However, in most programming languages, including Python, the order does matter.  

Whatever is on the left sign of the = symbol must be able to be assigned a value.  In Python this means it must be a variable.

Think of the = sign as an operator with a very low precedence.   A value passes from right to left across this operator.  In fact, in Python and some other languages may be used to "stack" assignments.  The following example is sometimes useful when more than one variable must be given the same value.

```
Python 3.9.5 (default, May 11 2021, 08:20:37) 
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x = y = 1+2
>>> x
3
>>> y
3
```