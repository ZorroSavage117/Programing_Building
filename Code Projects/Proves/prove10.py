# page start
print()

# varables
cart = []
prices = []
item = ""
price = 0.0
total = 0.0
menu_tf = True
menu = "Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit"
menu_select = ""

# main code

# menu
while menu_tf:
    print()
    print(menu)
    menu_select = input("Please enter an action: ")
    if menu_select == "1" or menu_select.lower() == "add item":
        # adding
        item = input("What item would you like to add? ")
        cart.append(item)
        price = float(input(f"What is the price of \'{item}\'? "))
        prices.append(price)
        print(f"\'{item}\' has been added to the cart.")
    elif menu_select == "2" or menu_select.lower() == "view cart":
        x = 0
        # for items in cart:
        # print(f"{items}")
        for items in cart:
            x += 1
            price = prices[x - 1]
            print(f"""{x}. {items} - {"{:.2f}".format(price)}""")
    elif menu_select == "3" or menu_select.lower() == "remove item":
        # print("Sorry this function not yet coded.")
        # removing
        item = input("Which item would you like to remove? ")
        y = int(item) - 1
        cart.pop(y)
        prices.pop(y)
        print("Item removed.")
    elif menu_select == "4" or menu_select.lower() == "compute total":
        # print("Sorry this function not yet coded.")
        # price total
        for x in prices:
            total += x
        print(
            f"""The total price of the items in the shopping cartis ${"{:.2f}".format(total)}""")
    elif menu_select == "5" or menu_select.lower() == "quit":
        print("Thank you. Goodbye.")
        menu_tf = False

# page end
print()
