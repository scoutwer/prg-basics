age = int(input("Enter your age: "))

if age >= 65:
    print("You are a Senior")
elif age >= 20:
    print("You are a Adult")
elif age > 13:
    print("You are a Teen")
else:
    print("You are a Child")