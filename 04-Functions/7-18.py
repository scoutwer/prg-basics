def f(num):
    list = {}
    result = 0 
    for j in str(num):
        if j in list:
            list[j] += 1
        else:
            list[j] = 1
    
    for k, i in list.items():
        if i > 1:
            result = result + i * int(list[k])
    return result


print(f(1223))
print(f(123))