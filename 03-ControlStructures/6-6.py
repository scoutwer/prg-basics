hours = int(input("Enter the amout of hours parked: "))

if hours > 6:
    print("Parking Fee: 20 PLN")
elif hours <=6 and hours >=3:
    print("Parking Fee: 15 PLN")
elif hours > 0 and hours <=2:
    print("Parking Fee: 5 PLN")