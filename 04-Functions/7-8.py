def f(num, bool):
    i = 0 
    result = 0 
    str_num = str(num)
    if bool == True:
        for i in range(len(str_num)):
            if int(str_num[i]) % 2 == 0:
                result = result + int(str_num[i])
    elif bool == False:
        for i in range(len(str_num)):
            if int(str_num[i]) % 2 == 1:
                result = result + int(str_num[i])
    return result

print(f(3124,True))
print(f(3124,False))
print(f(20576,True))
print(f(20576,False))
print(f(13115,True))



