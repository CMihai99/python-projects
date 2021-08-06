# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 6th, 2021

def convert(num):
    under_twenty = ("", "one ", "two ", "three ", "four ","five ",
    "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
    "twelve ", "thirteen ", "fourteen ", "fifteen ",
    "sixteen ", "seventeen ", "eighteen ", "nineteen ")

    under_hundred = ("", "", "twenty ", "thirty ", "forty ",
    "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")

    # Under zero (negative numbers)
    if num < 0:
        return "minus " + convert(-num)

    # Under twenty
    if num < 20:
        return under_twenty[num]

    # Under a hundred
    if num < 100:
        return under_hundred[num // 10] + under_twenty[int(num % 10)]

    # Under a thousand
    if num < 1000:
        return under_twenty[num // 100] + "hundred " + convert(int(num % 100))

    # Under a million
    if num < 1000000: 
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))

    # Under a billion
    if num < 1000000000:    
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))

    # Under a trillion
    if num < 1000000000000:
        return convert(num // 1000000000) + "billion " + convert(int(num % 1000000000))

    # Under a quadrillion
    if num < 1000000000000000:
        return convert(num // 1000000000000) + "trillion " + convert(int(num % 1000000000000))

    # Under a quintrillion
    if num < 1000000000000000000:
        return convert(num // 1000000000000000) + "quadrillion " + convert(int(num % 1000000000000))

    # Under a sextillion
    if num < 1000000000000000000000:
        return convert(num // 1000000000000000000) + "quintrillion " + convert(int(num % 1000000000000000))

    # Under a septillion
    if num < 1000000000000000000000000:
        return convert(num // 1000000000000000000000) + "sextillion " + convert(int(num % 1000000000000000000))

    # Under an octillion
    if num < 1000000000000000000000000000:
        return convert(num // 1000000000000000000000000) + "septillion " + convert(int(num % 1000000000000000000000))

    # Under a nonillion
    if num < 1000000000000000000000000000000:
        return convert(num // 1000000000000000000000000000) + "octillion " + convert(int(num % 1000000000000000000000000))

    # Under a decillion
    if num < 1000000000000000000000000000000000:
        return convert(num // 1000000000000000000000000000000) + "nonillion " + convert(int(num % 1000000000000000000000000000000))

    # Above a decillion
    return convert(num // 1000000000000000000000000000000000) + "decillion " + convert(int(num % 1000000000000000000000000000000000))

print(convert(int(input("Enter a number: "))))
