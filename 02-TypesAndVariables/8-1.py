# Calculation of circle area and circumference 
import math 

# determine radius and PI values

user_input = float(input("Radius: "))

# calculate area 

area = user_input * user_input * math.pi


# calculate circumference 

circumference = 2 * user_input * math.pi

# display results 

print(f'circumference: {round(circumference, 2)}')
print(f'Area: {round(area, 2)}')