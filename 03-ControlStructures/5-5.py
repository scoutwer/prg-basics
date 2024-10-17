###
# Sums numbers entered by user
#
total_sum = 0
i = 0 
while True:
    number = int(input("Enter a number (0 to stop): "))
    i += 1 
    if number == 0:
        i -= 1 
        break  # Exit the loop when 0 is entered
    else:
        total_sum += number

print(f"The total sum of the numbers is: {total_sum}")
print(f"The totals aritmethic sum of the numbers is: {total_sum / i}")