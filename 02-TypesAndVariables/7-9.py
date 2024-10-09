import random 

diced_rolled = random.randint(1, 6)
is_one  = diced_rolled == 1 or diced_rolled == 6

print(f'Special number (1 or 6): {is_one}')