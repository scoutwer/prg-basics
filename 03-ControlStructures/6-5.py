temperature =  int(input("Enter the Temperature: "))

if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature > 15:
    print("It is warm")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0 and temperature < 15:
    print("It is cold")
else:
    print("Warning, frost")