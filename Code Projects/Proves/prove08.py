# page start
print()

# variables
guess = ""
sec_word = "zorro"
hint = ""
count = 0
num_guess = 0
game_tf = True

# main code
# page set up
print("Welcome to the word Guessing game!\n")

# first inatal hint
while count != len(sec_word):
    hint = hint + "_ "
    count = count + 1
print(f"Your hint is: {hint}")

# the guessing game begins
while game_tf:
    # user input
    guess = input("What is your guess? ")
    num_guess = num_guess + 1

    # guess string is the correct length
    if len(guess) != len(sec_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess.lower() == sec_word:
        game_tf = False
    else:
        # hint code
        while count != len(sec_word):
            hint = hint + "_ "
            count = count + 1
        print(f"Your hint is: {hint}")

print("Congratulations! You guessed it!")
print(f"it took you {num_guess} guesses.")

# end page
print()
