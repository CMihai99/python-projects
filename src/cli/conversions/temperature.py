'''
Developed by: Calinescu Mihai
Date: 16 Mar, 2021

Github: https://github.com/CMihai99
'''

# CONVERTS: celsius, fahrenheit, kelvin


# Input
num1 = input('Enter the value: ')
unit1 = input('Convert from (celsius, fahrenheit, kelvin): ')
unit2 = input('To (celsius, fahrenheit, kelvin): ')

# Calculations

# Celsius
if unit1 == "celsius" and unit2 == "celsius":
    celsius = float(num1)
    ans = (celsius)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "celsius" and unit2 == "fahrenheit":
    celsius = float(num1)
    ans = (celsius*9/5)+32
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "celsius" and unit2 == "kelvin":
    celsius = float(num1)
    ans = (celsius)+273.15
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# Fahrenheit
if unit1 == "fahrenheit" and unit2 == "fahrenheit":
    fahrenheit = float(num1)
    ans = (fahrenheit)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "fahrenheit" and unit2 == "celsius":
    celsius = float(num1)
    ans = (celsius-32)*5/9
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "fahrenheit" and unit2 == "kelvin":
    kelvin = float(num1)
    ans = (kelvin-32)*5/9+273.15
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# Kelvin
if unit1 == "kelvin" and unit2 == "kelvin":
    kelvin = float(num1)
    ans = (kelvin)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kelvin" and unit2 == "celsius":
    celsius = float(num1)
    ans = (celsius)-273.15
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "kelvin" and unit2 == "fahrenheit":
    fahrenheit = float(num1)
    ans = (fahrenheit-273.15)*9/5+32
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)