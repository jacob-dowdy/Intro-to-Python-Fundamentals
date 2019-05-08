# function that takes an integer list and an index as arguments. 
# Depending on the value, function will replace selected index with "large" or "small".

def str_replace(int_list, index):
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list

str_replace([5,10,4,8], 2)
