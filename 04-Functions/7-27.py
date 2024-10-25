def f(num):
    result = "1"
    amount = num.count("1")
    for i in range(1,7):
        if num.count(str(i)) > amount:
            amount =  num.count(str(i))
            result = str(i)
    return result 


print(f("5233165554211"))
print(f("2133"))