from functools import reduce

numbers = [2,4,6,3,7,5]
e_num = filter(lambda x: x%2==0, numbers)
s_e = reduce(lambda x,y: x + y, e_num)

print(s_e)