###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math


def triangle_area(a,b,c):
    s = (a + b + c)/2 
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result


side_1 = float(input("Eneter a lenght of tside a: "))
side_2 = float(input("Eneter a lenght of t side b: "))
side_3 = float(input("Eneter a lenght of side c: "))



print(f'The area of ​​a triangle with sides {side_1}, {side_2}, {side_3} is {triangle_area(side_1, side_2, side_3)}' )
