# program that takes poem input from a user and mixes it up

def word_mixer(org_list):
    org_list.sort()
    new_words = []
    count = 0
    while len(org_list) > 5:
        new_words.append(org_list.pop(-5))
        new_words.append(org_list.pop(0))
        new_words.append(org_list.pop(-1))
    new_words = ' '.join(new_words)

    return new_words

user_input = input("enter a saying or poem: ")
words_list = user_input.split()
length = len(words_list)

for word in range(length):
    y = len(words_list[word])
    if y <= 3:
        words_list[word] = words_list[word].lower()
    elif y >= 7:
        words_list[word] = words_list[word].upper()
        
word_mixer(words_list)
    
