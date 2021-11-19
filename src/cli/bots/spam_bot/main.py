# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

import pyautogui

document = open("DOCUMENT.TXT", 'r')

for word in document:
    # Type selected document
    pyautogui.typewrite(word)
    # Send the message
    pyautogui.press("enter")
