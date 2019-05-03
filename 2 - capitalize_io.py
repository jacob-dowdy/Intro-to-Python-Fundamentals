# program that takes user's first name as input and capitalizes all "i"s and "o"s.

def capitalize_io():
    new_name = ""
    first_name = input("Enter your first name: ")
    for letter in first_name:
        if letter.lower() == "i" or letter.lower() == "o":
            new_name += letter.capitalize()
        else:
            new_name += letter
    print(new_name)
            
capitalize_io()
