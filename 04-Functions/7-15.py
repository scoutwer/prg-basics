def f(num):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    result = ""
    while count <= num -2 :
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        if count == num -2:
            result = next_number
    return result

print(f(5))
print(f(9))