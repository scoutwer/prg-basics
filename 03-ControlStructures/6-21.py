amount = int(input("Enter the amount in PLN: "))

num = amount
five_coins = 0
two_coins = 0 
one_coins = 0 

while True:
    if amount - 5 >=0:
        amount = amount - 5
        five_coins = five_coins + 1
    elif amount < 5 and amount > 1:
        amount = amount - 2 
        two_coins = two_coins + 1
    elif amount <= 1 and amount > 0:
        amount = amount - 1
        one_coins = one_coins + 1
    if amount == 0:
        break
print(f"The amount of PLN {num} in coins:")
print(f"5 PLN coins: {five_coins}")
print(f"2 PLN coins: {two_coins}")
print(f"1 PLN coins: {one_coins}")