# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

word = input("Enter word: ")

def palindrome(word):
    return word == word[::-1]

answer = palindrome(word)

if answer:
    print(f"Result: {word} is a palindrome")

else:
    print(f"Result: {word} is not a palindrome")
