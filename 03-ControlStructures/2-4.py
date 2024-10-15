###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
operator = input("Enter an operator: ")

if operator == "+":
    print(f'result: {number1 + number2}')
elif operator == "*":
    print(f'result: {number1 * number2}')
elif operator == "/":
    print(f'result: {number1 / number2}')
elif operator == "-":
    print(f'result: {number1 - number2}')
else:
    print("something went wrong")




