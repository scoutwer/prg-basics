###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]


middle = int( (len(arr))/2 - 1)
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('last value', arr[-1] )
print('sum', arr[0] + arr[-1])
print('midle value', arr[middle])

for i in arr:
    print(i , end= " ")