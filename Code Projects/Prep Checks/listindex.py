# page start
print()

# varables
cart = []
item = ""
item_num = 0
cart_tf = True

# main code
print("Please enter the items of the shopping list (type: quit to finish):")
# cart items input
while cart_tf:
    item = input("Item: ")
    if item.lower() == "quit":
        cart_tf = False
    else:
        cart.append(item)

# page set up
print()

# cart output 1
print("The shopping list is:")
for thing in cart:
    print(thing)

# print set up
print()

# cart output 2
print("The shopping list with indexes is:")
x = 0
for thing in cart:
    print(f"{x}. {thing}")
    x += 1

# page set up
print()

# item change
item_num = int(input("Which item would you like to change? "))
item = input("What is the new item? ")
cart[item_num] = item

# page set up
print()

# cart final output
print("The shopping list with indexes is:")
x = 0
for thing in cart:
    print(f"{x}. {thing}")
    x += 1

# page end
print()
