def min_pts(limit):
   return lambda pts: pts>=limit

arr = [37,51,44,23,78,92,39,84,83,51]
max_70 = list(filter(min_pts(70), arr))
max_40 = list(filter(min_pts(40), arr))
max_30 = list(filter(min_pts(30), arr))

print(f"Min 70 pts: {max_70}")
print(f"Min 40 pts: {max_40}")
print(f"Min 30 pts: {max_30}")