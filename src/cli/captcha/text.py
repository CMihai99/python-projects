'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


from captcha.image import ImageCaptcha

image = ImageCaptcha(width=300, height=100) # Image Captcha

user_input = input("Enter text to store as captcha: ") # Input

data = image.generate(user_input) # Generates text

image.write(user_input, 'texts/{}.png'.format(user_input)) # Writes file with dynamic filename