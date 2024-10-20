new_price = int(input("Current product price: "))
old_price = int(input("Previous product price: "))

amount_discounted = (old_price - new_price) / old_price * 100

if amount_discounted > 10:
    print("Buy the product!!")
    print(f"Product price reduced by {round(amount_discounted)}%")
else:
    print("It's not worth buying it now")