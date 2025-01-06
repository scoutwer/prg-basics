arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

new_arr = list(map(lambda x: f"{x[0].upper()}, {x[1]}", arr))
for i in new_arr:
    print(i)