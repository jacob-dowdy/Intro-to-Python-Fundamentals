# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))

print("numbers_1:",numbers_1)
print("numbers_2",numbers_2)
print("numbers 1 and 2 together: ", numbers_1 + numbers_2)


# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']

print("1st Row:", first_row)
print("2nd Row:", second_row)

first_row.extend(second_row)

print("Combined list is: ",first_row)

# [ ] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']

print("The first 3 rows of the Periodic table of elements contain: ", elem_1 + elem_2 + elem_3)
print("The row breakdown is: ")
print("Row 1:",", ".join(elem_1))
print("Row 2:",", ".join(elem_2))
print("Row 3:",", ".join(elem_3))

# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']

jack_jill.extend(next_line)
print(jack_jill)
