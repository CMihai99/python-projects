# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

word = input("Enter word: ")

def palindromeCheck(word):
    return word == word[::-1]

answer = palindromeCheck(word)

capitalized_word = word.capitalize()

if answer:
    print(f"Palindrome check: True. {capitalized_word} is a palindrome")

else:
    print(f"Palindrome check: False. {capitalized_word} is not a palindrome")
