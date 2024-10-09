import math 

entered_value = int(input("Enter tree circumference in cm: "))
tree =  entered_value / math.pi > 50 

print(f'Tree can be cut down: {tree}')
