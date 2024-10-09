
user_input = int(input("Enter a decimal number: "))
result_binary = ""

while user_input > 0:
    division = user_input%2 
    user_input = user_input // 2
    result_binary = result_binary + str(division)

print(f'Binary number: {result_binary[::-1]}')

