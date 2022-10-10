# page set up
print()

# variables
num1 = 0.0
num2 = 0.0
animal = ""

# main code

# number checker
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

# if statements for number checker
if num1 > num2:
    print("The first number is greater")
else:
    print("The first number is not greater")
if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
if num2 > num1:
    print("The second number is greater")
else:
    print("The second number is not greater")

# page set up
print()

# animal checker
animal = input("What is your favorite animal? ")

# if statement for animal checker
if animal.lower() in ("fox", "wolf", "cat"):
    print("That's my favorite anamil too!")
else:
    print("That one is not my favorite.")

# page set up
print()
