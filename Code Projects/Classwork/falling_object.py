# page set up
import math
print()

# varibles
mass = 0
gravity = 0
time = 0
cat = 0
density = 0
area = 0
drag_con = 0
velocity = 0
velocity_terminal = 0

# main code
# inputs
print("Welcome to the velocity calculator. Please enter the following: \n")
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(
    input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional area (in m^2): "))
drag_con = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

# calculations
cat = ((1/2) * density * area * drag_con)
velocity_terminal = math.sqrt((mass * gravity) / cat)
velocity = velocity_terminal * \
    (1 - math.exp((-math.sqrt(mass * gravity * cat) / mass) * time))

# outputs
print(f"""The inner value of c is: {"{:.3f}".format(cat)}""")
print(
    f"""The velocity after {time} seconds is: {"{:.3f}".format(velocity)} m/s""")
print(
    f"""The terminal velocity is: {"{:.3f}".format(velocity_terminal)} m/s""")

# page set up
print()
