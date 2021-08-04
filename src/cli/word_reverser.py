'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


def reverse_sentence(sentence):
    words = sentence.split(' ')                  #  Split string into words
    reverse_sentence = ' '.join(reversed(words)) # Reverse split string list and join using space  
    return reverse_sentence                      # Return joined string

# Run
if __name__ == "__main__":
    input = input("Enter sentence: ")
    print("Reversed sentence:", reverse_sentence(input))
