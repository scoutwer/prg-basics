###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    result = 0
    num = str(abs(number))
    for i in num:
        result = result + int(i)
    return result

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')