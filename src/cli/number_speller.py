'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


# Define numbers
def convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ",
             "six ", "seven ","eight ", "nine ", "ten ",
             "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ",
             "sixteen ", "seventeen ", "eighteen ", "nineteen ")

    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ",
           "sixty ", "seventy ", "eighty ", "ninety ")

# Convert numbers
    if num < 0:
        return "minus "+convert(-num)
    if num<20:
        return units[num] 
    if num<100:
        return  tens[num // 10]  +units[int(num % 10)] 
    if num<1000:
        return units[num // 100]  +"hundred " +convert(int(num % 100))
    if num<1000000: 
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))
    if num < 1000000000:    
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))
    return convert(num // 1000000000)+ "billion "+ convert(int(num % 1000000000))

print(convert(int(input("Enter a number: "))))
