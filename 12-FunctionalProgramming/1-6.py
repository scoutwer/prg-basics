avg = lambda x,y,z: x / (y + z/60)


distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours:"))
minutes = int(input("Enter number of travel minutes: "))

print(avg(distance,hours,minutes))

