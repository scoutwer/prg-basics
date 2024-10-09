###
# A program that displays your height both in cm and in feet and inches.
#
cm = int(input("Height: "))


# calculate the number of feet
inches = 3.28 * (cm/100) * 12
feet = 3.28 * (cm/100)


print(f'I am {cm}cm tall, i.e {feet} feet and {inches} inches')