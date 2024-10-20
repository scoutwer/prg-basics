article = input("Enter EAN-13 article number: ")

check = False

if len(article) == 13 and article.isdigit() == True:
    print("Article number is correct")
    check = True
else: 
    print("Incorrect article number")

if check == True and article[:3] == "590":
    print("Article manufactured in Poland")
elif check == True and article[:3] != "590":
    print("Article is not manufactured in Poland")