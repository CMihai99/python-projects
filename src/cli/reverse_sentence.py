# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

sentence = input("Enter sentence: ")

def reverse(sentence):
    words = sentence.split(' ')

    # Reverse split string and join using space
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print(f"Reversed sentence: {reverse(sentence)}")
