# Sorting

# Illustrates some more advanced sorting techniques

data = ["bob", "ted", "carol", "alice"]


def pickSecond(item):
    return item[1]


print(pickSecond("dog"))

print("\nOriginal order:")
print(data)

data.sort()
print("\nRegular sort")
print(data)

data.sort(reverse=True)
print("\nReversed source")
print(data)

data.sort(reverse=False, key=pickSecond)
print("\nSecond Character")
print(data)

data.sort(reverse=False, key=lambda x: x[2])
print("\nThird Character")
print(data)


