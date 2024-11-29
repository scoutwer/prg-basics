temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

mesaurements = len(temperatures)

negative = 0 
total_temp = 0
for i in temperatures:
    if i < 0: 
        negative = negative + 1
    total_temp = total_temp + i

avg = total_temp / mesaurements

min_t = min(temperatures)
max_t = max(temperatures)

print(mesaurements)
print(max_t)
print(min_t)
print(negative)
print(avg)
