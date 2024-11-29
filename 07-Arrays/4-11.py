def compare(array1, array2):
    result = True
    arr = []
    if len(array1) != len(array2):
        result = False
    else:
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                result = False
    print("Array1: ", end="")
    for i in array1:
        print(i, end=" ")
    print()
    print("Array2: ", end="")
    for j in array2:
        print(j, end=" ")
    print()
    if result == True:
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are not the same")

compare(["water","book","sky"], ["water","book","sky"])
compare([3,2,1], [3,2])