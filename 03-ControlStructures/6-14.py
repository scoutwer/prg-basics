facebook = False
twitter = True
instagram = False

num = 0 

while True:
    if facebook == True:
        num = num + 1 
    if twitter == True:
        num = num + 1
    if instagram == True:
        num = num + 1

    break

if num >= 2:
    print("You are a good influencer!")
else:
    print("You are not good influencer!")