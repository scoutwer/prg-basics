pin = "3467"
user_input = input("Enter the PIN code: ")
i =0
while True: 
    if user_input == pin:
        print("Correct PIN")
        break
    elif i > 1:
        print("Sorry, your payment card has been blocked.")
        break
    else:
        i+=1 
        print("Incorrect...")
        user_input = input("Enter the PIN code: ")
    

