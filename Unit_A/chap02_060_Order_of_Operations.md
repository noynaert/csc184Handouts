# 02.060 Order of operations

Mainly we are talking about Arithmetic operations here, but Order of Operations applies to all expressions.  

Python generally follows algebraic order of operations

Precedence | Operators|Examples
---|---|---
Paretheses|( )| (3 + 4) * 5
Exponentiation| ** | 2**3
Multiplication (and Division) | * / % //|5 * 2#<br>5 / 2<br>5 % 2<br>5 // 2
Addition (including Subtraction)| 5+2<br>5-2

## Operations at the same level

If operations have the same precedence they work left to right.  However Exponentiation works right to left.

```
>>> 2**3
8
>>> 2**3**2
512
>>> (2**3)**2
64
>>> 2**(3**2)
512
```

My advice is to use parenthesis when exponentiation is involved in all but trivial examples. 

## Negation

In many languages negation, like ```-5``` is considered a separate operation, and it has high precedence.  I am not finding documentation on this in Python.