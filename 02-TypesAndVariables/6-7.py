###
# A program that displays a numerical representation of each letter of your name.
#

name = "Krzysztof"
i = 0

while i < len(name):
    print(f'The letter {name[i]} has a code {ord(name[i])}')
    i = i + 1
    if i > len(name):
        break