# a program that takes a word as input and sorts the letters as odd or even depending on their index

odd_letters = []
even_letters = []
​
word = input("Enter a word: ")
​
for letter in range(0,len(word),2):
    odd_letters.append(word[letter])
    
for letter in range(1,len(word),2):
    even_letters.append(word[letter])
    
print(odd_letters)
print(even_letters)
