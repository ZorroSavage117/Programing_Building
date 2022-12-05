# page start
print()

# varaibles
str_in = ""

# functions


def display_regular(str):
    print(str)


def display_uppercase(str):
    output = str.upper()
    print(output)


def display_lowercase(str):
    output = str.lower()
    print(output)


# main code
str_in = input("What is your message? ")
display_regular(str_in)
display_uppercase(str_in)
display_lowercase(str_in)

# page end
print()
