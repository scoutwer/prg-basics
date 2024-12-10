t = (50,20,40,50,30,50)
value = int(input("value: "))

count = 0
for i in t:
    if i == value:
        count += 1

print(f"Number of occurrences: {count}")