# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    sum = 0 
    for i in cinema_seats:
        for j in i:
            sum = sum + len(j)
    return sum

def seats_available(seats):
    result = 0 
    for i in cinema_seats:
        for j in i:
            if j == "A":
                result = result + 1
    return result

def seats_booked(seats):
    result = 0 
    for i in cinema_seats:
        for j in i:
            if j == "B":
                result = result + 1
    return result

def seat_status(seats, row, place):
   if seats[row - 1][place-1] == "A":
       return "availabe"
   elif seats[row-1][place-1] == "B":
       return "booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5, 5))
print('Seat in row 3, place 5:',seat_status(cinema_seats,3,5))