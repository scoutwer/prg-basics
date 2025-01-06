Bottle_capacity = 500
Filling_tolerances = 0.02
Filling_tolerance = Bottle_capacity*Filling_tolerances
Filled_bottles = [508,500,512,499,492,511,503,476,501,509]


cor_fill = list(filter(lambda x: x > Bottle_capacity - Filling_tolerance and x < Bottle_capacity + Filling_tolerance, Filled_bottles))
per = 100 - round(len(cor_fill) / len(Filled_bottles)*100)
print(Bottle_capacity)
print(str(round(Filling_tolerances*100)) + "%")
print(Filled_bottles)
print(per)