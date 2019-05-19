# [ ] the list, elements_40, contains the names of the first 40 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_40
elements_40 = ['Hydrogen', \
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']

for num in range(0,len(elements_40),2):
  print(str(num + 1),"-",elements_40[num])
