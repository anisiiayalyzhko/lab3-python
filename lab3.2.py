word = str(input("Enter a word: "))

while not word.isalpha():
    word = str(input("Please enter a valid word containing only letters: "))

vowels = "aeiouAEIOU"

for letter in word:
    if letter in vowels:
        print(letter)

for letter in word:
    if letter not in vowels:
        print(letter)
