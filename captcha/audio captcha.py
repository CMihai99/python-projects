'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


from captcha.audio import AudioCaptcha

audio = AudioCaptcha() # Stores in an audio file

user_input = input("Enter text to store as audio (only numbers): ") # Input

data = audio.generate(user_input) # Generates data

audio.write(user_input, 'audio/{}.wav'.format(user_input)) # Writes file with dynamic filename