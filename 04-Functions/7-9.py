def f(x, y):
    result = 0
    for i in range(x, y):
        if i  < 0 and i%2 == 0:
            result = result + 1
    return result    



print(f(-7,8))
print(f(-1,11))