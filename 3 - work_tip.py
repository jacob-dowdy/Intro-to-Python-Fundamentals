# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "

work_tip = "Good code is commented code"
new_string = ""

for letter in work_tip:
    if letter == " ":
        new_string += "-"
    else:
        new_string += letter
    
print(new_string)
