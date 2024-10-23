def f(num):
    result = ""
    for i in range(1, num + 1):
        result = result + str(i)
    return result 

print(f(4))
print(f(11))