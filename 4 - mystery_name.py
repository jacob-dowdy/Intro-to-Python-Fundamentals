# a program that takes user input for a first name and does the following:
# - Reverses the name
# - replaces each "t","e", or "a" with a "?"

def mystery_name():
    first_name = input("What is your first name?: ")
    new_name = ""
    for letter in first_name[::-1]:
        if letter.lower() == "e" or letter.lower() == "t" or letter.lower() == "a":
            new_name += "?"
        else:
            new_name += letter
    print(new_name)

mystery_name()
