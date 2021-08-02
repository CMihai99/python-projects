'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


from vpython import *

canvas(background = color.white) # Change background color

base = ring(radius = 0.55, thickness = 0.35, color = vector(400, 100, 1))
topping = ring(radius = 0.85, thickness = 0.35, color = vector(0.4, 0.2, 0))

rad = 0 # Rotate donut

while True:
    rate(30) # Change rotation speed

    # Change rotation axis
    base.pos = vector(3*sin(rad), cos(rad), 1)
    topping.pos = vector(3*sin(rad), cos(rad), 1)
    rad = rad + 0.05
