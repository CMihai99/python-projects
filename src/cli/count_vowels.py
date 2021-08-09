# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

sentence = input("Enter sentence: ")

vowels = ["a", "A", "e", "E", "i", "I" "o", "O", "u", "U"]

count = 0

for char in sentence:
    if char in vowels:
        count = count + 1

if count = 1:
    print(f"Result: {count} vowel")

elif count > 1:
    print(f"Result: {count} vowels")
