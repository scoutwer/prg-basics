import json

product = {}

# read product data from keyboard
name = input("name: ")
price = round(float(input("price:")),2)
paid = input("paid: ")

if paid == "yes":
    paid = True
elif paid == "no":
    paid = False
else:
    raise ValueError(f"wrong paid answwer")

product["name"] = name
product["price"] = price
product["paid"] = paid

# save product data to json file
try:
    with open("product.json", 'r') as file:
        data = json.load(file)
except:
    data = []

data.append(product)

with open("product.json", 'w') as file:
        json.dump(data, file, indent = 4)