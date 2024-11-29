categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_cost = max(expenses)
index = expenses.index(max_cost)
print(categories[index])