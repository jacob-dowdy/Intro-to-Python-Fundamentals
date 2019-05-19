# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]
spell_len = len(spell_list)
half_1 = int(spell_len/2)

print("The first half of spell_list is: ")
for day in range(0,half_1):
    print(spell_list[day])
    
print("\nThe second half of spell_list is: ")
for day in range(half_1 - 1,spell_len):
    print(spell_list[day])
