def f(ob):
    result = 0 
    for i in ob:
        if result >= 3:
            return True
        if i in "+":
            result = result + 1
        elif i in "-":
            result = result - 1
    return False
    

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))