amount = int(input("Number of products purchased: "))
price = int(input("Product price: "))

if amount > 2: 
    recipt = 2 * price + (amount - 2) * price * 0.75
    print(f'Amount to pay: {recipt}')
elif amount <= 2:
    recipt = amount * price
    print(f'Amount to pay: {recipt}')