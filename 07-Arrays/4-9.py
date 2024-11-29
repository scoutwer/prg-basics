names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = names[0]

print(f"Names: ", end=" ")
for i in names:
    if len(i) > len(longest_name):
        longest_name = i
    print(i, end=" ")
print()
print(f"Longest name: {longest_name}")