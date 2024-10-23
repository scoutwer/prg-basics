def binary(num):
    for i in num:
        if i not in "01":
            return False
    return True



print(binary("101101"))
print(binary("1311a10100")) 