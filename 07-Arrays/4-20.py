def sort(data):
    for i in range(len(data)-1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                h = data[j]
                data[j] = data[j+1]
                data[j+1] = h
    return data

def second(data):
    return data[-2]

def dif(data):
    return [data[-1], data[0]]

def median(data):
    if len(data) % 2 != 0:
        return data[len(data)//2]
    else:
        num = len(data) / 2
        return (data[num] + data[num-1]) / 2

def f(data):
    ar = []
    ar.append(data[0])
    ar.append(data[-1])
    return ar


def string(data):
    result = ""
    for i in data:
        result = result + str(i) + "-"
    return result



arr = [7,3,8,5,2]

for i in arr:
    print("Numbers: ", end="")
    print(i, end=",")

print()
print(f"Second largest number: {second(sort(arr))}")
print()
print(f"Median: : {median(sort(arr))}")
print()

for i in sort(dif(arr)):
    print("Smallest and largest number:", end="")
    print(i, end="-")

print()
print(f"Numbers as a string: {string(sort(arr))}")