def f(arr):
    i = 0 
    j = 0 
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                h = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = h
    return arr



print(f([4,36,12,28,9,44,5]))