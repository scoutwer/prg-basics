arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
count = 0 

for i in arr:
    i[count] = i[count] + 1
    count = count + 1
    for j in i:
        print(j, end=" ")
    print()
