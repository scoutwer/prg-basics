user_input = int(input("Enter a decimal number: "))
result_binary = ""

while user_input > 0:
    division = user_input%16
    user_input = user_input // 16

    if division < 10:
        result_binary = result_binary + str(division)
    else:
        division = division + 55 
        result_binary = result_binary + chr(division)

print(f'Binary number: {result_binary[::-1]}')