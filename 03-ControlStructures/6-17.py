hour = input("Enter time (24-hour format): ").split(":")

if int(hour[0]) > 12:
    hour[0] = int(hour[0]) - 12
    print(f"Time in 12-hour format: {hour[0]}:{hour[1]}pm")
else: 
    print(f"Time in 12-hour format: {hour[0]}:{hour[1]}am")
