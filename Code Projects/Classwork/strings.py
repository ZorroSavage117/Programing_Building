# page start
print()

# variables
stig = "commitment"
inlet = ""
words = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
count = 0
innum = 0
game = True
cont = ""

# main code
# rewuirment 1 and 2
inlet = input("Choose your letter: ")
for letter in stig:
    if letter.lower() == inlet.lower():
        print(inlet.upper(), end="")
    else:
        print(letter.lower(), end="")

# page set up
print("\n")

# requirment 3
for letter in stig:
    if letter.lower() == inlet.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")

# page set up
print("\n")

# strech challenge
while game:
    innum = int(input("Choose your number (1-9): "))
    for letter in words:
        if count == innum:
            print(letter.upper(), end="")
            count = 0
        else:
            print(letter.lower(), end="")
            count += 1
    print("\n")
    cont = input("Do you want to play again? ")
    if cont.lower() == "n" or cont.lower() == "no":
        game = False

# page end
print("\n")
