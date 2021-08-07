# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 7th, 2021

sentence = input("Enter sentence: ")

def reverse(sentence):
    words = sentence.split(' ') # Split string into words
    reverse_sentence = ' '.join(reversed(words)) # Reverse split string and join using space  
    return reverse_sentence # Return joined string

print(f"Reversed sentence: {reverse(sentence)}")
