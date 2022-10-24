# page set up
import random
print()

# variables
my_num = random.randint(1, 100)
guess = 0
run_tf = True
guess_num = 0

# main code
while run_tf:
    guess = int(input("What is your guess? "))

    if guess > my_num:
        print("Lower")
    elif guess < my_num:
        print("Higher")
    elif guess == my_num:
        print("You got it.")
        run_tf = False

    guess_num = guess_num + 1

print(f"It took you {guess_num} tries")

# page set up
print()
