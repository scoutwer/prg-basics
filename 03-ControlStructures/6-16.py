###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
is_spin = False
is_rinse = False
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:').lower()
extra_rinse = input('Extra rinse? (y/n)').lower()
extra_spin = input('Extra spin? (y/n)').lower()

if program == "j" or "jacket":
    total_washing_time = total_washing_time + 40
elif program == "u" or "underwear":
    total_washing_time = total_washing_time +  70
elif program == "s" or "shoes":
    total_washing_time = total_washing_time +  20
else:
    print("Something went wrong")

if extra_rinse == "y":
    total_washing_time = total_washing_time + 15
    is_rinse = True
if extra_spin == "y":
    total_washing_time = total_washing_time + 9
    is_spin = True 

print(f'rinse = {is_rinse}')
print(f'spin = {is_spin}')
print(f'Total washing time: {total_washing_time} minutes')

