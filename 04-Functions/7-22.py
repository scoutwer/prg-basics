def f(txt):
    if len(txt) < 6:
        return False
    else:
        for i in txt:
            if txt.count(i) > 1:
                return False
    return True



print(f("ax15"))
print(f("A2water3"))
print(f("book123"))
print(f(""))
print(f("qwerty"))