n = 1

while n <= 30:
    if n % 3 == 0 and n % 5 == 0:
        print("BINGO", end= " ")
    elif n%3 == 0:
        print("THREE", end= " ")
    elif n%5 == 0:
        print("FIVE", end= " ")
    else:
        print(n, end= " ")
    n = n + 1 
