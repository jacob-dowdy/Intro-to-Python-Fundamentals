# short program that uses string indexing to check for i,o, and u as second letter in a team name.
team_name = input("What's the second letter of your favorite team?: ")

if team_name[1].lower() == "i":
    print("The second letter of your favorite team is \"i\"")
elif team_name[1].lower() == "o":
    print("The second letter of your favorite team is \"o\"")
elif team_name[1].lower() == "u":
    print("The second letter of your favorite team is \"u\"")
else:
    print("The second letter is not i,o, or u.")
