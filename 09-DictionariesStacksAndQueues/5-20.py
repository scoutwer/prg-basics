import json

with open("reservations.json", 'r', encoding="utf-8") as file:
    data  = json.load(file)


def rooms(dic):
    return len(dic["reservations"])

def paid(dic):
    arr = []
    for i in dic["reservations"]:
        if i["paid"]:
            arr.append(i)
    return len(arr)

def un_paid(dic):
    arr = []
    for i in dic["reservations"]:
        if not i["paid"]:
            arr.append(i)
    return len(arr)

def value(dic):
    arr = []
    for i in dic["reservations"]:
        if i["paid"]:
            arr.append(i["price_per_night"]* i["nights"])
    return sum(arr)

def un_paid_value(dic):
    arr = []
    for i in dic["reservations"]:
        if not i["paid"]:
            arr.append(i["price_per_night"]* i["nights"])
    return sum(arr)


print(rooms(data))
print(paid(data))
print(un_paid(data))
print(un_paid(data))
print(value(data))
print(un_paid_value(data))