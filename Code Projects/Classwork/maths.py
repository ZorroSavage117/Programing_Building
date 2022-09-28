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

# main code
length1 = float(input("What is the length of a side of the squrare? "))
sqr_area = length1 ** 2
print(f"the area of the square is: {sqr_area}")
length1 = float(input("What is the length of rectangle? "))
width1 = float(input("What is the width of the rectangle? "))
rct_area = length1 * width1
print(f"The area of the rectangle is: {rct_area}")
radius1 = float(input("What is the radius of the circle? "))
crl_area = math.pi * (radius1 ** 2)
print(f"The are of the circle is: {crl_area}")
print()
length1 = float(input("What is the length of a side? "))
sqr_area = length1 ** 2
crl_area = math.pi * (length1 ** 2)
cube_vol = length1 ** 3
sphere_vol = (4 / 3) * math.pi * (length1 ** 3)
print(
    f"The area of the square is: {sqr_area} \nThe area of the circle is: {crl_area} \nThe volume of the cube is: {cube_vol} \nThe volume of the sphere is: {sphere_vol}")

# page set up
print()
