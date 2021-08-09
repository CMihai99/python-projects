# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

def translate():
    characters = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

    sentence = input('Enter sentence: ')
    sentence = sentence.split()

    # Translate sentence to pig latin
    for k in range(len(sentence)):
        i = sentence[k]

        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = i + 'ay'

        elif t(i) in characters:
            sentence[k] = i[2:] + i[:2] + 'ay'

        elif i.isalpha() == False:
            sentence[k] = i

        else:
            sentence[k] = i[1:] + i[0] + 'ay'

    return ' '.join(sentence)

def t(str):
    return str[0] + str[1]

if __name__ == "__main__":
    x = translate()

    print(f"Pig latin translation: {x}")
