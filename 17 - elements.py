# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']

for num in range(1,len(elements),2):
    print(str(num + 1),"-",elements[num])
