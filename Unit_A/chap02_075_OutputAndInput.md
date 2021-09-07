# 02.75 Output and Input

## Output

* The `print` function is the workhorse of output.  
* It has several forms, but we will only consider two simple ones
* A major difference between Python2 and Python3 is that Python3 requires parenthesis around the data being printed

### Printing single items

```
temperature = 32
print(temperature)
print("Hello, World")
```

### Printing more than one thing at a time

You may separate items to be printed with commas.  The commas will become blank spaces on the output.

```
print ("The temperature is",temperature,"Fahrenheit)
```

## Input

The `input()` function gets input from the keyboard.

***The input() method returns a string***

```python
print("What is your name?")
name = input()
print("Hello,",name)
```

The prompt may be included in the input. You need to add a blank for spacing.

```python
name = input("What is your name? ")
print("Hello,"name)
```

If you want to get a number it must be converted from a string to the correct type of number.

```python
s = input("How many feet? ")
feet = float(s)
s = input("How many degrees fahrenheit?)
fahrenheit = int(s)
```

The entire conversion may be done by combining the statements

```python
feet = float(input("How many feet? "))
fahrenheit = int(input("How many degrees fahrenheit? "))