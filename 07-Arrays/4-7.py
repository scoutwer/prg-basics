i = 0 
arr = [15, 8, 31, 47, 2, 19]

arithmetic = 0
while i < len(arr):
    arithmetic = arithmetic + arr[i]
    print(arr[i], end = " ")
    i = i + 1 
print()
print(int(arithmetic/len(arr)))