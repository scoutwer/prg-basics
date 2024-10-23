def vending(amount):
    coins = 0
    while True:
        if amount - 5 >=0:
            amount = amount - 5
            coins = coins + 1
        elif amount < 5 and amount > 1:
            amount = amount - 2 
            coins = coins + 1
        elif amount <= 1 and amount > 0:
            amount = amount - 1
            coins = coins + 1
        if amount == 0:
            break
    return coins


print(vending(23))
print(vending(8))
print(vending(2))
print(vending(0))