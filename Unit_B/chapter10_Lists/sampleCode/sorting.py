#demonstrates sorting. 

fruits = ["grape","banana","fig","mango","date","cherry","grapefruit",
          "strawberry", "apple", "kiwi", "pinapple", "orange"]

def printList(array, n):
    print("---------------")
    for i in range(n):
        print(f"[{i:2}] {array[i]}")
    print("---------------")

printList(fruits, len(fruits))
fruits.sort()
printList(fruits, len(fruits))
