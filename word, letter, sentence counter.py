'''
Developed by: Calinescu Mihai
Date: 6 Apr, 2021

Github: https://github.com/CMihai99
'''


import time

# Input
paragraph = input("Enter paragraph: ")

# Word Counter
res = len(paragraph.split())
# Print result
time.sleep(0.5)
if res <= 1:
    print("Number of words in the paragraph: " + str(res), "word") # If there is less than 1 word, print singular form
elif res > 1:
    print("Number of words in the paragraph: " + str(res), "words") # Else if there are more words than 1, print plural form

# Letter Counter
res = len(paragraph)
# Print result
time.sleep(0.5)
if res <= 1:
    print("Number of characters in the paragraph (including spaces): " + str(res), "character") # If there is less than 1 character, print singular form
elif res > 1:
    print("Number of characters in the paragraph (including spaces): " + str(res), "characters") # Else if there are more characters than 1, print plural form

# Sentence Counter
res = len(paragraph.split('.'))
# Print result
time.sleep(0.5)
if res <= 1:
    print("Number of sentences in the paragraph: " + str(res), "sentence") # If there is less than 1 sentence, print singular form
elif res > 1:
    print("Number of sentences in the paragraph: " + str(res), "sentences") # Else if there are more sentences than 1, print plural form