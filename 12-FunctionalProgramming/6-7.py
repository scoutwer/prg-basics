arr = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

new_arr = list(map(list,arr))

for i in new_arr:
    i.remove(max(i))
    i.remove(min(i))

res = list(map(lambda x: sum(x), new_arr))
print(res)