# Developed by: Calinescu Mihai <mihaimihaia431@gmail.com>
# Date: August 6th, 2021

def convert(num):
    under_twenty = ("", "one ", "two ", "three ", "four ",
    "five ", "six ", "seven ", "eight ", "nine ", "ten ",
    "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
    "sixteen ", "seventeen ", "eighteen ", "nineteen ")

    under_hundred = ("", "", "twenty ", "thirty ", "forty ",
    "fifty ", "sixty ", "seventy ", "eighty ", "ninety ")

    # Under zero
    if num < 0:
        return f"minus {convert(-num)}"

    # Under twenty
    if num < 20:
        return under_twenty[num]

    # Under a hundred
    if num < 100:
        return under_hundred[num // 10] + under_twenty[int(num % 10)]

    # Under a thousand
    if num < 1000:
        return under_twenty[num // 100] + f"hundred {convert(int(num % 100))}"

    # Under a million
    if num < 1000000: 
        return convert(num // 1000) + f"thousand {convert(int(num % 1000))}"

    # Under a billion
    if num < 1000000000:    
        return convert(num // 1000000) + f"million {convert(int(num % 1000000))}"

    # Under a trillion
    if num < 1000000000000:
        return convert(num // 1000000000) + f"billion {convert(int(num % 1000000000))}"

    # Under a quadrillion
    if num < 1000000000000000:
        return convert(num // 1000000000000) + f"trillion {convert(int(num % 1000000000000))}"

    # Under a quintrillion
    if num < 1000000000000000000:
        return convert(num // 1000000000000000) + f"quadrillion {convert(int(num % 1000000000000))}"

    # Under a sextillion
    if num < 1000000000000000000000:
        return convert(num // 1000000000000000000) + f"quintrillion {convert(int(num % 1000000000000000))}"

    # Under a septillion
    if num < 1000000000000000000000000:
        return convert(num // 1000000000000000000000) + f"sextillion {convert(int(num % 1000000000000000000))}"

    # Under an octillion
    if num < 1000000000000000000000000000:
        return convert(num // 1000000000000000000000000) + f"septillion {convert(int(num % 1000000000000000000000))}"

    # Under a nonillion
    if num < 1000000000000000000000000000000:
        return convert(num // 1000000000000000000000000000) + f"octillion {convert(int(num % 1000000000000000000000000))}"

    # Under a decillion
    if num < 1000000000000000000000000000000000:
        return convert(num // 1000000000000000000000000000000) + f"nonillion {convert(int(num % 1000000000000000000000000000000))}"

    # Above a decillion
    return convert(num // 1000000000000000000000000000000000) + f"decillion {convert(int(num % 1000000000000000000000000000000000))}"

print(convert(int(input("Enter a number: "))))
