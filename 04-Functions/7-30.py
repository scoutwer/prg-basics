
def f(x, n):

    if n == 0:
        return 1 
    else:
        return x * f(x, n-1)
    

print(f(5,3))