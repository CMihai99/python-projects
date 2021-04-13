'''
Developed by: Calinescu Mihai
Date: 16 Mar, 2021

Github: https://github.com/CMihai99
'''

# CONVERTS: usd, ron, eur, gbp


# Input
num1 = input('Enter the value: ')
unit1 = input('Convert from (usd, ron, eur, gbp): ')
unit2 = input('To (usd, ron, eur, gbp): ')

# Calculations

# USD
if unit1 == "usd" and unit2 == "usd":
    usd = float(num1)
    ans = (usd)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "usd" and unit2 == "ron":
    ron = float(num1)
    ans = (ron)*4.11
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "usd" and unit2 == "eur":
    eur = float(num1)
    ans = (eur)*0.84
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "usd" and unit2 == "gbp":
    gbp = float(num1)
    ans = (gbp)*0.72
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# RON
if unit1 == "ron" and unit2 == "ron":
    ron = float(num1)
    ans = (ron)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ron" and unit2 == "usd":
    usd = float(num1)
    ans = (usd)*0.24
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ron" and unit2 == "eur":
    eur = float(num1)
    ans = (eur)*0.2
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "ron" and unit2 == "gbp":
    gbp = float(num1)
    ans = (gbp)*0.18
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# EUR
if unit1 == "eur" and unit2 == "eur":
    eur = float(num1)
    ans = (eur)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "eur" and unit2 == "usd":
    usd = float(num1)
    ans = (usd)*1.19
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "eur" and unit2 == "ron":
    ron = float(num1)
    ans = (ron)*4.89
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "eur" and unit2 == "gbp":
    gbp = float(num1)
    ans = (gbp)*0.86
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

# GBP
if unit1 == "gbp" and unit2 == "gbp":
    gbp = float(num1)
    ans = (gbp)*1
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "gbp" and unit2 == "eur":
    eur = float(num1)
    ans = (eur)*1.17
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "gbp" and unit2 == "usd":
    usd = float(num1)
    ans = (usd)*1.39
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)

elif unit1 == "gbp" and unit2 == "ron":
    ron = float(num1)
    ans = (ron)*5.70
    formatted_ans = "{:.4f}".format(ans)
    print(formatted_ans, unit2)