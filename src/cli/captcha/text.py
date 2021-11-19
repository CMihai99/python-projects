# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: November 19th, 2021

from captcha.image import ImageCaptcha

user_input = input("Enter text to store as captcha: ")
data = image.generate(user_input)

image = ImageCaptcha(width=300, height=100)
image.write(user_input, 'texts/{}.png'.format(user_input))
