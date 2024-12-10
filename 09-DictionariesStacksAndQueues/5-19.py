import json

with open("dogs.json", 'r', encoding="utf-8") as file:
    data  = json.load(file)


arr = []
for dog in data:
    if dog["age"] < 5:
        arr.append(dog)


for i in arr:
    for key, value in i.items():
        print(f"{key}: {value}")
    print()