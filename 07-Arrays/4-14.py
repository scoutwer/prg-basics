arr=[2,3,2,5,8,1,9,8]
li = []

print("Array: ", end="")
for i in arr:
    if arr.count(i) == 1:
        li.append(i)
    print(i, end=" ")

print()
print("Unique elements: ", end="")
for j in li:
    print(j, end=" ")

