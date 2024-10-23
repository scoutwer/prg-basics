def in_range(num, x, y):
    result = "No"
    for i in range(x, y):
        if i == num:
            result = "yes"
    return result    

number = int(input("A number: "))
x = int(input(" X (of range <x, Y>): "))
y = int(input(" Y (of range <x, Y>): "))

print(f'Number {number} in the range <{x},{y}>: {in_range(number, x, y)}')