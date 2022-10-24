# page set up
import random
print()

# variables
my_num = 0
my_num_end = 0
guess = 0
cont = ""
run_tf = True
game_tf = True
guess_num = 0
total_guesses = 0
num_games = 0
gpg = 0

# main code
while game_tf:

    my_num_end = random.randint(100, 1000000)
    my_num = random.randint(1, my_num_end)
    guess = 0
    guess_num = 0

    print(f"Guess a number between 1 and {my_num_end}")

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

    cont = input("Do you want to play agian? ")

    if cont.lower() == "no":
        game_tf = False
    else:
        run_tf = True

    num_games = num_games + 1
    total_guesses = total_guesses + guess_num

gpg = total_guesses / num_games
print(f"You played {num_games}.")
print(f"Your total number of guesses was {total_guesses}.")
print(f"Your guesses per game was {gpg}")

# page set up
print()
