# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

from captcha.audio import AudioCaptcha

user_input = input("Enter text to store as audio (only numbers): ")
data = audio.generate(user_input)

audio = AudioCaptcha()
audio.write(user_input, 'audio/{}.wav'.format(user_input))
