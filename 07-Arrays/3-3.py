# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
x = 0
sum_cost = 0 
first_category = 0 
second_category = 0 
third_category = 0 
costs= []
for i in monthly_expenses:
    costs.append(sum(i))
    first_category = first_category + i[0]
    second_category  = second_category + i[1]
    third_category = third_category + i[2]

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', first_category)
print('Transport:',second_category)
print('Utilities:',third_category)
print('Week 1:',costs[0])
print('Week 2:',costs[1])
print('Week 3:',costs[2])
print('Week 4:',costs[3])
print('---------------')
print('TOTAL:',sum(costs))