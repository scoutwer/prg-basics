arr = []
for i in range(1,21):
    arr.append(i)

divisible = list(filter(lambda x: x%2 == 0 and x%3 == 0, arr))

for item in divisible:
    print(item)