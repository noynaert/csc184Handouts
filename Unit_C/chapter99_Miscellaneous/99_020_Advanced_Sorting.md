#  99.020 Advanced Sorting

## Review

```python
data = ["bob", "ted", "carol", "alice"]

print("\nOriginal order:")
print(data)

# Regular sort
data.sort()
print("\nRegular sort")
print(data)
```

Output is

```text
Original order:
['bob', 'ted', 'carol', 'alice']

Regular sort
['alice', 'bob', 'carol', 'ted']
```

## Reversing

Reversing may be useful, but mainly we are doing it to get to the next field.

```python
data.sort(reverse=True)
print("\nReversed source")
print(data)
```

## Sorting with a custom function call

For strings or numbers, sort does a normal comparison.  However, we can also provide the name of a function that returns a single value for one item on the list.  The sort() function will call that function for each item on the list and do the comparison based on the returned value.  

Here is a function that returns the second letter of a string.

```python
def pickSecond(item):
    return item[1]

...

data.sort(reverse=False, key=pickSecond)
print("\nSecond Character")
print(data)    
```

Output is

```text
Second Character
['carol', 'ted', 'alice', 'bob']
```

## Lambda

A lambda is a very shorthand way to write very simple functions.  In the following example x represents the value being processed.

The following uses a lambda function to return the third character from the string.

```python
data.sort(reverse=False, key=lambda x: x[2])
print("\nThird Character")
print(data)
```

Output

```text
Third Character
['bob', 'ted', 'alice', 'carol']
```
