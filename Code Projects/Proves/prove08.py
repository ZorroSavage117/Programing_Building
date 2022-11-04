# page start
import random
print()

# variables
guess = ""
list_words = ["mountaindew", "mountain", "dew", "zorro"]
hint = ""
num_guess = 0
total_guess = 0
num_games = 0
game_tf = True
redo_tf = True

# main code
# page set up
print("Welcome to the word Guessing game!\n")

# do you wish to play again
while redo_tf:

    # game reset
    game_tf = True

    # word selected
    sec_word = random.choice(list_words)

    # first inatal hint
    hint = ""
    for letter in sec_word:
        hint = hint + "_ "
    print(f"Your hint is: {hint}")

    # the guessing game begins
    num_guess = 0
    while game_tf:

        # user input
        guess = input("What is your guess? ")
        guess = guess.lower()
        num_guess = num_guess + 1

        # guess string is the correct length and if the letters are in and if they match up
        if len(guess) != len(sec_word):
            print(
                "Sorry, the guess must have the same number of letters as the secret word.")
        elif guess.lower() == sec_word:
            game_tf = False
        elif len(guess) == len(sec_word):
            hint = ""
            y = 0
            for letter in guess:
                x = sec_word.find(letter)
                # print(f"{x}  {y}")
                if x == y:
                    hint += letter.upper()
                elif x <= len(sec_word) and x != -1:
                    hint += letter.lower()
                else:
                    hint += "_"
                y += 1

            # hint code
            print(f"Your hint is: {hint}")

    # when the round has finished
    print("Congratulations! You guessed it!")
    print(f"it took you {num_guess} guesses.\n")
    guess = input("Do you want to play again? ")
    if guess.lower() == "no" or guess.lower() == "n":
        redo_tf = False
    num_games += 1
    total_guess += num_guess

# when finised play game and all the rounds
print(f"It took you {num_games} rounds and a total of {total_guess} guesses, you avarge guess per round was {total_guess / num_games}")
# end page
print()


# helpful code from teach
# my_string = "shit"
# new_string = ""
# for letter in my_string:
#     print(letter)
# for letter in my_string:
#     if letter == "s":
#         new_string += "z"
#     else:
#         new_string += letter
# print(new_string)
