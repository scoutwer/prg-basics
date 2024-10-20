decimal_number = int(input("Enter decimal number: "))
num = decimal_number
binary_number = ""

while decimal_number > 0:
    binary_number = binary_number + str(decimal_number % 2)
    decimal_number = decimal_number // 2 
print(f'{num}(10) = {binary_number[::-1]}(2)')
