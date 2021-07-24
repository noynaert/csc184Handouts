# Chapter 02 -- Part 010 -- Numbers and Numeric Operators

This chapter covers some of the things that the book covers in chapter 1.

## Numeric Data Types

$ has three types of numbers

* ***int*** Int is short for "integer."  SInts are whole numbers that do not have decimal points
* ***float*** Float numbers have decimal points.
* ***complex*** Python has native representation of complex numbers.  We will not use complex numbers.

## int

* Whole numbers
* Math on int values is usually very fast
* Ints may be written in decimal (base 10), octal (base 8), hexadecimal (base 16), and binary (base 2).  *For now we will only used base 10 or decimal.  Don't panic if you don't know what this is talking about*
* Int literals may start with
  * + and - signs (plus and minus).
  * digits 1 through 9.  You cannot start a decimal int with a 0.
  * int numbers may not be written with commas.  For example, 1 million written as 1,000,000 does not work as you might expect it (feel free to test it in interactive mode).  However, you may use _ symbols in place of commas.  So 1 million may be written as 1_000_000)
  * int values are precise.  There is no rounding in the computer when using integers unless the programmer explicitly tells Python to round.

## float

* Floats are rational numbers.
* Math with floats is generally slower than integers.
* The precision of floats is 15 digits on most modern systems.
    * *There can be rounding error when using floats* 
* Floats have decimal points
* Floats may be represented in scientific notation.  100.00 may be written as 1.e2 We won't use scientific notation at the moment, but be aware it exists because it will sometimes pop up in weird places
* on most system ints may be from about -2 billion to +2 billion.

## The ```type()``` function

The parenthesis indicates that type is a function.

"Arguments" or "Parameters" go inside the parenthesis.

The type function returns the data type Python is using for that expression.

What does each of the following print when you type it into the interpreter?

    type(7)
    type(7.)
    type(1.e2)

## Arithmetic Operators (a very short list)

Symbol | Meaning
:---:|:--
+|Addition
-|Subtraction
*|Multiplication
/|Division (Always returns a float)
**|Exponentiation

#### Operators and Data Type

When two integers are added, subtracted, or multiplied the result is an integer.  Exponentiation involving integers also returns an integer.

When two integers are divided with / the result is converted to a float.

```
>>> 5/2
2.5
```

If the arithmetic involves mixed types (int and float) then the result is a float.

```
>>> 5 + 0
5
>>> 5 + 0.
5.0
```

### Forcing type conversion with a "Cast"

A cast is used to force a type conversion.

The int() function converts the type of a number to an integer and float() converts the type of a number into a real number.

The int() function ***truncates*** the fractional part of the number.  It *does not round.*

```
>>> int(2.)
2
>>> int(2.2)
2
>>> int(2.5)
2
>>> int(2.999999)
2
>>> int(-2.999)
-2
```

### More Arithmetic Operators

The following are additional operators that are commonly used.

Symbol | Meaning
:---:|:---
%|Mod  (Gives the remainder.  For now only use with int)
//|Integer Division

