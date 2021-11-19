# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

sentence = input("Enter sentence: ")

consonants = ["b", "B", "c", "C", "d", "D", "f", "F",
"g", "G", "h", "H", "j", "J", "k", "K", "l", "L", "m", "M",
"n", "N", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T",
"v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]

count = 0

for char in sentence:
    if char in consonants:
        count = count + 1

if count = 1:
    print(f"Result: {count} consonant")

elif count > 1:
    print(f"Result: {count} consonants")
