###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input("enter last letter: ")
first_letter_code = int(ord(first))
last_letter_code = int(ord(last))

if last == first:
    print(f'Between {first} and {last} is 0 letters')
else:
    number_of_letters = last_letter_code - first_letter_code - 1
    print(f'Between {first} and {last} is {number_of_letters} letters')