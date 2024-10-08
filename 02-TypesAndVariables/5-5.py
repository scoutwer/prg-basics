price = float(input("price: "))
discount = float(input("Discount: "))

amount_of_discount = round(price * (discount/100), 2 )
price_ad = round(price - amount_of_discount, 2) 


print("Price after discount: ", price_ad)
print("Discount: ", amount_of_discount)