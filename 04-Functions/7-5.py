def card(num):
    if len(num) != 16 or num.isdigit() == False:
        return "wrong card number"
    else:
        result = num[:2] + 10 * "*" + num[-4:]
        return result
    

print(card("5290312400019022"))

print(card("52903124000190"))
print(card("5290312400019a22"))