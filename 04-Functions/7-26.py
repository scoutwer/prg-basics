def f(num):
    fourth_digit = 0
    if len(num) != 4 and num.isdigit() == False:
        return False 
    else:
        for i in range(3):
            fourth_digit = fourth_digit + int(num[i])
        if num[-1] != str(fourth_digit%7):
            return False
        else:
            return True


print(f("1082"))
print(f("2035"))
print(f("1114") )     
print(f("7071"))