# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [ ] use list addition to concatenate the lists into all_num and print
zero_nine = []
ten_onehundred = []

for number in range(1,10):
    zero_nine.append(number)
    
for number in range(10,101,10):
    ten_onehundred.append(number)
    
print("The zero_nine list contains:", zero_nine)
print("The ten_onehundred list contains:", ten_onehundred)

together = zero_nine + ten_onehundred

print(together)
