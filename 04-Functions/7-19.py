def num(n):
    num = 0 
    result=[]
    count = 0
    while count < n:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0: 
                    break
            else:
                count = count + 1
                result.append(num)
        num = num + 1 
    return result[-1]



print(num(5))
print(num(1))