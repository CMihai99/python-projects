'''
Developed by: Calinescu Mihai
Date: 14 Mar, 2021

Github: https://github.com/CMihai99
'''


# Import Required Packages
import pyttsx3
import PyPDF2

# Define Document
document = open('oop.pdf', 'rb')
documentReader = PyPDF2.PdfFileReader(document)
pages = documentReader.numPages
speaker = pyttsx3.init()

# Tell Speaker To Read From Document
for num in range(0, pages):
    page = documentReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
