a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

cube_volume = a*b*c
cube_surface_area = a*c*2 + b * a*2 + b*c*2

print(f'The volume of a cube with sides {a}, {b}, {c} is {cube_volume}')
print(f'The surface area of a cube with sides {a}, {b}, {c} is {cube_surface_area}')