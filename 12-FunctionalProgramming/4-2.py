speeds = input("Recorded values: ").split(",")
over_speed = list(filter(lambda e: int(e) > 50, speeds))

print("Speed too high:" , end=" ")
for i in over_speed:
    print(i, end=" ")