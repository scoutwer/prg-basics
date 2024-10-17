###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

entered_pin = input("Enter your PIN: ")

while True:
    if entered_pin != pin:
        print("Wrong PIN")

        entered_pin = input("Enter your PIN: ")
    else:
        break

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("3. Withdraw")
    print("4. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-4): ")
    print()


    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == "4":
        new_pin = input("Enter new PIN: ")
        while True: 
            if new_pin.isdigit() == False or len(new_pin) != 4:
                print()
                print("Wrong Pin")
                print()
                new_pin = input("Enter new PIN: ")
            else:
                print("You have sucesfully changed your PIN")
                print()
                break
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
