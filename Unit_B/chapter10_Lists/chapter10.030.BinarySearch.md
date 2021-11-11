# 10.030 Binary Search

Binary search requires an array to be sorted.

Binary search cuts a list in half and determines which half of the array would contain the item we are looking for.  This cutting in half continues until the item is located or the search area is empty.

## Sorting


```python
fruits = ["grape","banana","fig","mango","date","cherry","grapefruit",
          "strawberry", "apple", "kiwi", "pineapple", "orange"]

def printList(array, n):
    print("---------------")
    for i in range(n):
        print(f"[{i:2}] {array[i]}")
    print("---------------")

printList(fruits, len(fruits))
fruits.sort()
printList(fruits, len(fruits))
```

The sort routine is case sensitive.  Upper case letters will always sort ahead of lowercase.


## Binary search algorithm

The following is an algorighm written in *pseudocode.*  Pseduocode conveys the ideas about the steps involved without worrying about syntax details.  The algorithm could be coded into many different languages.  

```text
function binarySearch(haystack, needle)
    foundAt=-1  #-1 indicates not found
    first = 0
    last = len(haystack)-1

    while( first <= last and foundAt < 0)
       mid = (first + last) // 2
       if haystack[mid] == needle
          foundAt = mid
       else
          if needle < haystack[mid]
             last = mid - 1
          else
             first = mid + 1
    return foundAt
```

The Growth Rate of a binary search is O(Log<sub>2</sub> n) where n is the number of items on the list.

## Reference
[https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php](https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php)