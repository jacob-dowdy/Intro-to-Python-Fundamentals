# python program that reverses the items in a list

some_numbers =[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]

reverse_list = []

while some_numbers:
    # pops the first item in the existing list
    popped_number = some_numbers.pop(0)
    # puts the popped item at the beginning of the reversed list
    reverse_list.insert(0, popped_number)
print(reverse_list)
