# page set up
print()

# variables
choice = ""
restart = "y"

# main code
choice = input("Do you want to play a game? Yes - No - Maybe\n")

# you are playing no mater what you choose
if choice.lower() == "no":
    print("Your lying...")
elif choice.lower() == "maybe":
    print("Yes you do!")
elif choice.lower() == "yes":
    print("I have the perfect game for you.")
else:
    print("Your playing anyways.")

# the game begins
while restart == "y":
    choice = input(
        "You are in a dark room, you see a shadow of a (MANTLE - FOOTBOARD) in the dim light coming through the window.\n")

    # living room or bedroom
    if choice.lower() == "mantle":
        # level 2: living room
        while restart == "y":
            choice = input(
                "You are in the living room of an unknow house. You try to find (PHONE - LIGHTSWICH) first.\n")

            # phone or ligthswich
            if choice.lower() == "phone":
                print(
                    "You find no phone but you do find a lightswich. Turn on the lights? (YES - NO)\n")
                restart = "n"
            else:
                print(
                    "Try again but use one of the all caps words but I like your stile...")
                restart = "y"
    elif choice.lower() == "footboard":
        # level 2: bedroom
        while restart == "y":
            choice = input(
                "You are in a bedroom that you do not recanize. You (LEAVE - STAY) the bed that you are laying in.\n")

            # leave stay or yeal
            if choice.lower() == "yeal":
                print("(Hidden path) You screem at the top of you lungs and you wake up back in you bed in your own room. It was just a nightmare.")
                restart = "n"
            else:
                print(
                    "Try again but use one of the all caps words but I like your stile, do you feel like YEALing.")
                restart = "y"
    else:
        print("Try again but use one of the all caps words but I like your stile...")
        restart = "y"

# page set up
print()
