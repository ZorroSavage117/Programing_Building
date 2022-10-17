# page set up
print()

# variables
height1 = 0
height1_tf = False
age1 = 0
age1_tf = False
height2 = 0
height2_tf = False
age2 = 0
age2_tf = False
golden1 = ""
golden2 = ""
golden1_tf = False
golden2_tf = False
can_ride = False
can_ride1 = False
can_ride2 = False

# main code

# first rider questions
age1 = int(input("What is the age of the first rider? "))
golden1 = input("Does the rider have a golden passport (yes/no)? ")
height1 = int(input("What is the height of the first rider? "))
second_rider = input("Is there a second rider (yes/no)? ")

# second rider questions
if second_rider.lower() == "yes":
    age2 = int(input("What is the age of the second rider? "))
    golden2 = input("Does the rider have a golden passport (yes/no)? ")
    height2 = int(input("What is the height of the second rider? "))
    second_rider = True

# age requierment or golden tickit
# rider 1
if age1 >= 18:
    age1_tf = True
elif golden1.lower() == "yes" and (12 <= age1 < 18):
    golden1_tf = True
# rider 2
if age2 >= 18:
    age2_tf = True
elif golden2.lower() == "yes" and (12 <= age2 < 18):
    golden2_tf = True

# height requierment
# rider 1
if height1 >= 36:
    height1_tf = True
# rider 2
if height2 >= 36:
    height2_tf = True

# can ride or not
if height1_tf and height2_tf:
    if age1_tf or golden1_tf or height2_tf or age2_tf or golden2_tf:
        can_ride = True
    else:
        if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
            can_ride = True
        elif (age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
            can_ride = True
        else:
            can_ride = False
else:
    if (age1_tf or golden1_tf) and height1 >= 62:
        can_ride = True
    else:
        can_ride = False

# output
if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")

# page set up
print()
