items = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
count = 0 
for key in items:
    print(f"{key}: {items[key]}")
    count = count + items[key]

print(f"Total items: {count}")