def occurs(number, array): 
    if number in array:
        return number, array, True
    else: 
        return number, array, False
res = occurs(55, [15,38,7,23,14])

print(f"Number: {res[0]}",)
print("Array: ", end="")
for i in res[1]:
    print(i, end=" ")
print()
if res[2] == True:
    print(f"Result: number {res[0]} appears in the array")
else:
    print(f"Result: number {res[0]} does not appear in the array")




