# page set up
print()

# varables
pos_neg = -1
candy = ""
there_yet = ""
run_tf = True

# main code
# positive number
while pos_neg < 0:
    pos_neg = int(input("Please type a positive number: "))

    if pos_neg < 0:
        print("Sorry, that in a negative number. Please try again.")
    else:
        print(f"The number is: {pos_neg}")

# page set up
print()

# candy
while run_tf:
    candy = input("May I have a piese of candy? ")

    if candy.lower() == "yes":
        print("Thank you.")
        run_tf = False

# page set up
print()

# are we there yet
run_tf = True

while run_tf:
    there_yet = input("Are we there yet? ")

    if there_yet.lower() == "yes":
        print("Ok.")
        run_tf = False

# page set up
print()
