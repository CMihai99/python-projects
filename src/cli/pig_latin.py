'''
Developed by: Calinescu Mihai
Date: 16 Mar, 2021

Github: https://github.com/CMihai99
'''


import time

def main():
        characters = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']

        # Input
        sentence = input('Enter sentence: ')
        sentence = sentence.split()
        time.sleep(0.5)
        print("Translating to Pig Latin...")
        time.sleep(0.8)

        # Translate sentence into pig latin
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i+'ay'
                elif t(i) in characters:
                        sentence[k] = i[2:]+i[:2]+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:]+i[0]+'ay'
        return ' '.join(sentence)

def t(str):
        return str[0]+str[1]

# Run
if __name__ == "__main__":
        x = main()
        print(x)
