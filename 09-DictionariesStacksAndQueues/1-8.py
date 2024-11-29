price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

count = 0 

for key in price_list:
    print(f"{key}: {price_list[key]}")
    count = count + price_list[key]
print(round(count, 2))

new_c = 0

for key in price_list:
    price_list[key] = round(0.9*price_list[key],2)
    new_c = new_c + price_list[key]
    print(f"{key}: {price_list[key]}")

print(round(new_c, 2))

