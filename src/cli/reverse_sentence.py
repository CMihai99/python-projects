# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 5th, 2021

string = input("Enter sentence: ")

def reverse_sentence(sentence):
    words = sentence.split(' ')  # Split string into words
    reverse_sentence = ' '.join(reversed(words)) # Reverse split string and join using space  
    return reverse_sentence  # Return joined string

print("Reversed sentence:", reverse_sentence(string))
