'''
Developed by: Calinescu Mihai
Date: 18 Jan, 2021

Github: https://github.com/CMihai99
'''


import pyautogui, time

time.sleep(0.5)
f = open("loremipsum.txt", 'r') # Select document

for word in f:
    pyautogui.typewrite(word)   # Type the document selected line by line
    pyautogui.press("enter")    # And press enter so send the message
