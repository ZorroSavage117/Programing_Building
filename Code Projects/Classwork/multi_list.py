# page start
print()

# varaibles
names = []
balances = []
name = ""
balance = 0.0
in_tf = True
total = 0.0
ave = 0.0

# main code
# input
print("Enter the names and balances of bank accounts (type: quit when done)")
while in_tf:
    name = input("What is the name of this account? ")
    if name == "quit":
        in_tf = False
    else:
        names.append(name)
        balance = float(input("What is the balance? "))
        balances.append(balance)

# page set up
print()

# outputs
# account info
print("Account Information")
x = 0
for title in names:
    print(f"""{title} - ${"{:.2f}".format(balances[x])}""")
    x += 1

# page set up
print()

# totals and avarage
for y in balances:
    total += y

ave = total / len(balances)

print(f"""Total: {"{:.2f}".format(total)}""")
print(f"""Average: {"{:.2f}".format(ave)}""")

# page end
print()
