import csv

registration = {}

with open("vehicle.txt", 'r') as file:
    text = file.read()
    l = []
    l = text.split()

    for i in l:
        if i[0] not in registration.keys():
            registration[i[0]] = 1
        else:
            registration[i[0]] += 1

    with open("province.csv",'r', encoding="utf-8") as f:
        content = csv.reader(f)
        for line in content:
            for key in registration:
                if line[0] == key:
                    print(line[1],": ", registration[key])
