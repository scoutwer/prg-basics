
total = 0 
with open('pets.txt', 'r') as file:
    for line in file:
        arr = line.split()
        total = total + len(arr)
        print(line, end = "")
    print()
    print("number of words: ", total)