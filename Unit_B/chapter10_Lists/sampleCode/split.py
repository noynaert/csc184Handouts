# illustrates split

line = "  Twas brillig and the slithy toves Did gyre and gimble in the wabe   ".strip().lower()

words = line.split()

for word in words:
    print(word)