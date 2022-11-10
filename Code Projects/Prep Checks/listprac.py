# page start
print()

# variables
names = []
name_tf = True
info = ""

# main code
# input
while name_tf:
    info = input("Type the name of a friend: ")
    if info.lower() == "end":
        name_tf = False
    else:
        names.append(info)

# page set up
print()

# output
print("Your friends are:")
for name in names:
    print(name)

# page end
print()
