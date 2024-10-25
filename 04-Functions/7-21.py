def f(txt):
    res = txt.split()
    result = ""
    if len(res) == 1:
        return res[0][0].upper()
    else:
        for i in range(len(res)):
            result = result + res[i][0]
        return result.upper()


    
print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))