# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurace of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]
pt_1 = 0
pt_2 = 0
pt_3 = 0

for basket in baskets:
    if basket == 1:
        pt_1 += 1
    elif basket == 2:
        pt_2 += 1
    elif basket == 3:
        pt_3 += 1
        
print("There were",pt_1,"one pointers made.")
print("There were",pt_2,"two pointers made.")
print("There were",pt_3,"three pointers made.")
