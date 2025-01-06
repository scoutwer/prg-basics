arr = []
for i in range(1,21):
    arr.append(i)
power = list(map(lambda x: x**3,arr))
for i in range(len(power)):
    print(f"{arr[i]}:{power[i]}")