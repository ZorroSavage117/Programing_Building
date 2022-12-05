# page set up
import math
print()

# varibaes
length1 = 0
width1 = 0
radius1 = 0
sqr_area = 0
rct_area = 0
crl_area = 0
cube_vol = 0
sphere_vol = 0

# functions


def compute_area_square(x):
    z = x ** 2
    return z


def compute_area_rectangle(x, y):
    z = x * y
    return z


def compute_area_circle(x):
    z = math.pi * (x ** 2)
    return z


def compute_vol_cube(x):
    z = x ** 3
    return z


def compute_vol_sphere(x):
    z = (4 / 3) * math.pi * (x ** 3)
    return z


# main code
length1 = float(input("What is the length of a side of the squrare? "))
sqr_area = compute_area_square(length1)
print(f"the area of the square is: {sqr_area}")

length1 = float(input("What is the length of rectangle? "))
width1 = float(input("What is the width of the rectangle? "))
rct_area = compute_area_rectangle(length1, width1)
print(f"The area of the rectangle is: {rct_area}")

radius1 = float(input("What is the radius of the circle? "))
crl_area = compute_area_circle(radius1)
print(f"The area of the circle is: {crl_area}")

print()

length1 = float(input("What is the length of a side? "))
sqr_area = compute_area_square(length1)
crl_area = compute_area_circle(length1)
cube_vol = compute_vol_cube(length1)
sphere_vol = compute_vol_sphere(length1)
print(f"""The area of the square is: {sqr_area}
The area of the circle is: {crl_area}
The volume of the cube is: {cube_vol}
The volume of the sphere is: {sphere_vol}""")

# page set up
print()
