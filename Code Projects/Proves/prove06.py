# page set up
print()

# variables
choice = ""
restart = True

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
# level 1: waking up
while restart:
    choice = input(
        "You are in a dark room, you see a shadow of a (MANTLE - FOOTBOARD) in the dim light coming through the window.\n")

    # living room or bedroom
    if choice.lower() == "mantle":
        # level 2: living room
        while restart:
            choice = input(
                "You are in the living room of an unknow house. You try to find (PHONE - LIGHTSWITCH) first.\n")

            # phone or ligthswitch
            if choice.lower() == "phone":
                # level 3: the switch
                while restart:
                    choice = input(
                        "You find no phone but you do find a lightswitch. Turn on the lights? (YES - NO)\n")

                    # yes or no
                    if choice.lower() == "yes":
                        # level 4: the ending - bad
                        print("""You turn on the light to see your body in a recliner and its all bloodly and missing your head... \nSorry to say this but looks like death has comes for you.""")
                        restart = False
                    elif choice.lower() == "no":
                        # level 4: the ending - ok
                        print("""You don't flip the switch on a hunch, but then you see the Grim Reaper come through the window...\nHe is here for you, to take you to the after life.""")
                        restart = False
                    else:
                        print(
                            "Try again but use on of the all caps words, thank you.")
                        restart
            elif choice.lower() == "lightswitch":
                # level 3: the good switch
                while restart:
                    choice = input(
                        "You flip the switch, you see a door and a window that leads to a field of corn. You go through the (DOOR - WINDOW)\n")

                    # door or window
                    if choice.lower() == "door":
                        # level 4: the ending - bad dream
                        print("""You open the door, as you do so something comes fli=ying at your face...\nYou wake up back in your bed relevid that it was only a nightmare.""")
                        restart = False
                    elif choice.lower() == "window":
                        # level 4: the ending - good dream
                        print("""You climb out the window and run for the fleid of corn , but as you reach the fleid you start seeing light...\nThe light that you are seeing is daylight as you wake up in your bed nice and warm.""")
                        restart = False
                    else:
                        print(
                            "Try again but use one of the all caps words, thank you.")
                        restart
            else:
                print(
                    "Try again but use one of the all caps words but I like your stile...")
                restart
    elif choice.lower() == "footboard":
        # level 2: bedroom
        while restart:
            choice = input(
                "You are in a bedroom that you do not recanize. You (LEAVE - STAY) the bed that you are laying in.\n")

            # leave stay or yell
            if choice.lower() == "leave":
                # level 3: hallway
                while restart:
                    choice = input(
                        "You find a hallway that is empty. You (RUN - WALK) down the hallway.\n")

                    # run or walk
                    if choice.lower() == "run":
                        # level 4: the ending - extream bad
                        print("""You deside to run down the hallway, but as you do so you feel like some thing is ripping you apart with each step.\nYou notice that your fingers are disipaering at each joint moving to your shoulder its very painful.\nEvetualy you are all missing except for your head =, you are missing your jaw though, and you hear a voice, it says,\n\"I told you not to run\"\nAs everything fades to black it than fades to white as you open your eyes relieezing that it was just a dream.""")
                        restart = False
                    elif choice.lower() == "walk":
                        # level 4: the ending - good
                        print("""As you walk down the hall everything fades to black as you wake up in a hospital bed surronded by family...\nThey rejoice and expain to you that you were in a coma for two years.""")
                        restart = False
                    else:
                        print("Try again but use on of the all caps words, thank you")
                        restart = False
            elif choice.lower() == "stay":
                # level 3: bedroom continued
                while restart:
                    choice = input(
                        "You decide to stay. Do you go back to (BED) or do you stay (AWAKE)?\n")

                    # bed or awake
                    if choice.lower() == "bed":
                        # level 4: the ending - ok
                        print(
                            "You go back to bed ag go to sleep. You wake up next to your specal someone. THE END.")
                        restart = False
                    elif choice.lower() == "awake":
                        # level 4: the ending - unknown
                        print(
                            "As you stay up all night you relize that you are now stuck in this reality with no way to escape... THE END...")
                        restart = False
                    else:
                        print(
                            "Try again but use one of the all caps words, thank you.")
                        restart
            elif choice.lower() == "yell":
                # level 3: hidden ending
                print("(Hidden path) You screem at the top of you lungs and you wake up back in you bed in your own room. It was just a nightmare.")
                restart
            else:
                print(
                    "Try again but use one of the all caps words but I like your stile, do you feel like YELLing.")
                restart
    else:
        print("Try again but use one of the all caps words but I like your stile...")
        restart

# page set up
print()
