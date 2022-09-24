# Page set up
print()

# Variables
adjective1 = "unknown"
animal1 = "unknown"
verb1 = "unknown"
exclamation1 = "unknown"
verb2 = "unknown"
verb3 = "unknown"
exclamation2 = "unknown"
verb4 = "unknown"
name1 = "unknown"
noun1 = "unknown"
verb5 = "unknown"
story = "unknown"

# Main code
print("Please enter the following:\n")
adjective1 = input("adjective: ")
animal1 = input("animal: ")
verb1 = input("verb: ")
exclamation1 = input("exclam1ation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
exclamation2 = input("exclamation: ")
verb4 = input("verb: ")
name1 = input("name: ")
noun1 = input("noun: ")
verb5 = input("verb: ")
story = input("a or b: ")

print(f"\nYour story is: {story}\n")

if story.lower() == "a":
    print(f"""The other day, I was really in trouble. It all started when I saw a very 
{adjective1} {animal1} {verb1} down the hallway. \"{exclamation1.capitalize()}\" I yelled. But all 
I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3}
right in front of my family. Then my sister yelled, \"{exclamation2.upper()}!\" As my sister said this, mother {verb4} me.
Uncle {name1} grabed the {noun1} and {verb5} out the door.""")
elif story.lower() == "b":
    print(f"""The {adjective1} man ran in to a {animal1} on his {verb1} to the store. \"{exclamation1.capitalize()}\", he exclamed.
He began to {verb2} at the sight, to no {verb3} nothing happened. He than said, \"{exclamation2.capitalize()}.\" So he {verb4}
on and went to {name1}\'s Market. He when to buy a {noun1}, it was important so he could {verb5}.""")
else:
    print(f"Invalid story ID -- {story} is not one of the options")

# Page set up
print()
