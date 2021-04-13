'''
Developed by: Calinescu Mihai
Date: 6 Apr, 2021

Github: https://github.com/CMihai99
'''


# Import packages
import time

# Input
sentence = input("Enter the sentence: ")
string = sentence.lower()

# Vowel Counter
# Create Variables
count = 0
vowels = ["a", "e", "i", "o", "u"]

# Count Vowels
for char in string:
    if char in vowels:
        count = count+1

# Print result
time.sleep(0.5)
if count <= 1:
    print("Number of vowels in given sentence is:", count, "vowel")
elif count > 1:
    print("Number of vowels in given sentence is:", count, "vowels")


# Consonant Counter
# Create Variables
count = 0
consonants = ["b", "c", "d", "f", "g",
              "h", "j", "k", "l", "m",
              "n", "p", "q", "r", "s",
              "t", "v", "w", "x", "y", "z"]

# Count Vowels
for char in string:
    if char in consonants:
        count = count+1

# Print result
time.sleep(0.5)
if count <= 1:
    print("Number of consonants in given sentence is:", count, "consonant")
elif count > 1:
    print("Number of consonants in given sentence is:", count, "consonants")