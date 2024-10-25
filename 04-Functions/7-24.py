   
def f(txt):
    result = ""
    if len(txt) < 1:
        return ""
    else:
        for i in txt:
            result = result + i + "-"
        return result[:-1]



print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))