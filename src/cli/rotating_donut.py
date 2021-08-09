# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 9th, 2021

from vpython import *

canvas(background = color.white, width = 1520, height = 705)

base = ring(radius = 0.55, thickness = 0.35, color = vector(400, 100, 1))

topping = ring(radius = 0.85, thickness = 0.35, color = vector(0.4, 0.2, 0))

# Rotation
rad = 0

while True:
    # Rotation speed
    rate(30)

    # Rotation axis
    base.pos = vector(3*sin(rad), cos(rad), 1)

    topping.pos = vector(3*sin(rad), cos(rad), 1)

    rad = rad + 0.05
