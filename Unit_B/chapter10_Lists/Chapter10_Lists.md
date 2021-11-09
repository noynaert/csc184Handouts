# Chapter 10 Lists

In many other languages lists are called "arrays."  Lists and arrays generally operate in the same ways, although each language does have its idiosyncrasies.

* Like strings, lists are a *sequence.*
* Lists are *mutable*
* Strings and lists are both sequences, and sometimes we use similar notation to deal with them.  However, in Python, strings are not just arrays of characters.

## Example

```python
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in days:
    print(day)
```


## The `range()` function

Range has three different forms.

### Form 1: stop

In its simplest form, `range(5)` produces a sequence of numbers from 0 through 4.   Note that this is something like how string slices work.

```python
print("range(7)")
for r in range(7):
    print (r)
```

Produces

```text
0
1
2
3
4
5
6
```

### Form 2: start, stop

Range may take two arguments to specify a start value and a stop value.  Note that the range goes up to the stop value but does not include it.

```python
print("\n 3 to 5")
for r in range(3,5):
    print(r)
```
Produces

```text
 3 to 5
3
4
```

### Form 3: start, stop, step

The third version of the range has a start, stop, and step.  

```python
print("\n2 to 10 by 2's")
for r in range(2,10,2):
    print(r)
  
print("\n0 to 10 by 3's")
for r in range(0,10,3):
    print(r)
```

Produces:
```text
2 to 10 by 2's
2
4
6
8

0 to 10 by 3's
0
3
6
9
```

## Traversing lists with ranges

```python
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# traversing with an index
for i in range(len(days)):
    print(f"Day {i} is {days[i]}")
```

## Lists are *mutable*

We can change the value in any element of the array.

```python
days[1] = "Lunes"
print("Day[1] is now ",days[1])
for day in days:
    print(day)
```

Produces the following.  Note that Monday has now been replaced.

```text
Sunday
Lunes
Tuesday
Wednesday
Thursday
Friday
Saturday
```