# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

word = input("Enter word: ")

def palindromeCheck(word):
    return word == word[::-1]

answer = palindromeCheck(word)

if answer:
    print("Word is a palindrome")

else:
    print("Word isn't a palindrome")
