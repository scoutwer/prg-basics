def f(txt):
    if txt[::-1] == txt:
        return True
    else:
        return False
    
print(f("radar"))
print(f("12-11-21"))
print(f("book"))