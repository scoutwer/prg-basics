import random


arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr10 = [4,0,3]
arr11 =[]
arr12 = [i for i in range(1,30)]
arr13 = []
arr14 = []
for i in range(15):
    arr11.append(0)


i = 0 
while i < 20 :
    arr13.append(random.randint(0,1))
    i = i + 1
for x in range(5):
    arr14.append([])
    for j in range(2):
        arr14[x].append(False)


print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(arr14)
