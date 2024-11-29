file_name = input("File name: ")
lines = 0
characters = 0 
words = 0 
try:
    with open(file_name, "r") as file:
        for line in file:
            characters = characters + len(line)
            arr = line.split()
            words = words + len(arr)
            lines = lines + 1 
    print(f"Number of lines: {lines}")
    print(f"Number of characters: {characters}")
    print(f"Number of words: {words}")
except FileNotFoundError:
    print("Wrong file")

