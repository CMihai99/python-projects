# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

import pyttsx3, PyPDF2

document = open('oop.pdf', 'rb')
documentReader = PyPDF2.PdfFileReader(document)
pages = documentReader.numPages
speaker = pyttsx3.init()

# Read document
for num in range(0, pages):
    page = documentReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
